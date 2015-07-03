Name:           ros-indigo-fetch-calibration
Version:        0.6.1
Release:        0%{?dist}
Summary:        ROS fetch_calibration package

Group:          Development/Libraries
License:        Apache2
URL:            http://ros.org/wiki/fetch_calibration
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-robot-calibration >= 0.5.1
BuildRequires:  ros-indigo-catkin

%description
Launch and configuration files for calibrating Fetch using the
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

* Sun May 31 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.5.4-1
- Autogenerated by Bloom

