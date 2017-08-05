Name:           ros-indigo-freight-calibration
Version:        0.7.12
Release:        0%{?dist}
Summary:        ROS freight_calibration package

Group:          Development/Libraries
License:        Apache2
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-robot-calibration
BuildRequires:  ros-indigo-catkin

%description
Launch and configuration files for calibrating Freight using the
'robot_calibration' package.

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
        -DCMAKE_INSTALL_LIBDIR="lib" \
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
* Sat Aug 05 2017 Michael Ferguson <mferguson@fetchrobotics.com> - 0.7.12-0
- Autogenerated by Bloom

* Tue Jul 26 2016 Michael Ferguson <mferguson@fetchrobotics.com> - 0.7.9-0
- Autogenerated by Bloom

* Mon Jul 18 2016 Michael Ferguson <mferguson@fetchrobotics.com> - 0.7.8-0
- Autogenerated by Bloom

