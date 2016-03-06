Name:           ros-indigo-fetch-depth-layer
Version:        0.7.3
Release:        0%{?dist}
Summary:        ROS fetch_depth_layer package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-costmap-2d
Requires:       ros-indigo-cv-bridge
Requires:       ros-indigo-image-transport
Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-opencv-candidate
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-costmap-2d
BuildRequires:  ros-indigo-cv-bridge
BuildRequires:  ros-indigo-image-transport
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-opencv-candidate
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs

%description
The fetch_depth_layer package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sat Mar 05 2016 Michael Ferguson <mferguson@fetchrobotics.com> - 0.7.3-0
- Autogenerated by Bloom

* Wed Feb 24 2016 Michael Ferguson <mferguson@fetchrobotics.com> - 0.7.2-0
- Autogenerated by Bloom

* Wed Jan 20 2016 Michael Ferguson <mferguson@fetchrobotics.com> - 0.7.1-0
- Autogenerated by Bloom

* Tue Sep 29 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.7.0-0
- Autogenerated by Bloom

* Thu Jul 30 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.6.2-0
- Autogenerated by Bloom

* Fri Jul 03 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.6.1-0
- Autogenerated by Bloom

* Tue Jun 23 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.6.0-0
- Autogenerated by Bloom

* Fri Jun 19 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.5.14-0
- Autogenerated by Bloom

* Sat Jun 13 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.5.13-0
- Autogenerated by Bloom

* Fri Jun 12 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.5.12-0
- Autogenerated by Bloom

* Wed Jun 10 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.5.11-0
- Autogenerated by Bloom

* Sun Jun 07 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.5.10-0
- Autogenerated by Bloom

* Sun Jun 07 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.5.9-0
- Autogenerated by Bloom

* Sun Jun 07 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.5.8-0
- Autogenerated by Bloom

* Fri Jun 05 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.5.7-0
- Autogenerated by Bloom

* Thu Jun 04 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.5.6-0
- Autogenerated by Bloom

* Wed Jun 03 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.5.5-0
- Autogenerated by Bloom

