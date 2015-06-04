Name:           ros-indigo-fetch-depth-layer
Version:        0.5.5
Release:        0%{?dist}
Summary:        ROS fetch_depth_layer package

Group:          Development/Libraries
License:        CreativeCommons-Attribution-NonCommercial-NoDerivatives-4.0
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
* Wed Jun 03 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.5.5-0
- Autogenerated by Bloom

