#!/usr/bin/env python

# Copyright (c) 2015, Fetch Robotics Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the Fetch Robotics Inc. nor the names of its
#       contributors may be used to endorse or promote products derived from
#       this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL FETCH ROBOTICS INC. BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
# THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# Author: Michael Ferguson

import subprocess
from threading import Thread

import rospy
from sensor_msgs.msg import Joy
from moveit_msgs.msg import MoveItErrorCodes
from moveit_python import MoveGroupInterface

class MoveItThread(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.start()

    def run(self):
        self.process = subprocess.Popen(["roslaunch", "fetch_moveit_config", "move_group.launch"])
        _, _ = self.process.communicate()

    def stop(self):
        self.process.send_signal(subprocess.signal.SIGINT)
        self.process.wait()

def is_moveit_running():
    output = subprocess.check_output(["rosnode", "info", "move_group"], stderr=subprocess.STDOUT)
    if output.find("unknown node") >= 0:
        return False
    if output.find("Communication with node") >= 0:
        return False
    return True

def tuck():
    if not is_moveit_running():
        rospy.loginfo("starting moveit")
        move_thread = MoveItThread()

    rospy.loginfo("Waiting for MoveIt...")
    client = MoveGroupInterface("arm_with_torso", "base_link")
    rospy.loginfo("...connected")

    joints = ["torso_lift_joint", "shoulder_pan_joint", "shoulder_lift_joint", "upperarm_roll_joint",
              "elbow_flex_joint", "forearm_roll_joint", "wrist_flex_joint", "wrist_roll_joint"]
    pose = [0.05, 1.32, 1.40, -0.2, 1.72, 0.0, 1.66, 0.0]
    while not rospy.is_shutdown():
        result = client.moveToJointPosition(joints, pose, 0.0, max_velocity_scaling_factor=0.5)
        if result.error_code.val == MoveItErrorCodes.SUCCESS:
            move_thread.stop()
            return

class TuckArmTeleop:

    def __init__(self):
        self.tuck_button = rospy.get_param("~tuck_button", 6)  # default button is the down button
        self.tucking = False

        self.pressed = False
        self.pressed_last = None

        self.joy_sub = rospy.Subscriber("joy", Joy, self.joy_callback)

    def joy_callback(self, msg):
        if self.tucking:
            # only run once
            return
        try:
            if msg.buttons[self.tuck_button] > 0:
                if not self.pressed:
                    self.pressed_last = rospy.Time.now()
                    self.pressed = True
                elif self.pressed_last and rospy.Time.now() > self.pressed_last + rospy.Duration(1.0):
                    # Tuck the arm
                    self.tucking = True
                    tuck()
                    # Stopping the MoveIt thread works, however, the action client
                    # does not get shut down, and future tucks will not work.
                    # As a work-around, we die and roslaunch will respawn us.
                    rospy.signal_shutdown("done")
                    exit(0)
            else:
                self.pressed = False
        except KeyError:
            rospy.logwarn("tuck_button is out of range")

if __name__ == "__main__":
    rospy.init_node("tuck_arm")
    t = TuckArmTeleop()
    rospy.spin()
