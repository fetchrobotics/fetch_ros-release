Name:           ros-indigo-fetch-ros
Version:        0.7.15
Release:        0%{?dist}
Summary:        ROS fetch_ros package

Group:          Development/Libraries
License:        BSD
URL:            https://docs.fetchrobotics.com/
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-fetch-calibration
Requires:       ros-indigo-fetch-depth-layer
Requires:       ros-indigo-fetch-description
Requires:       ros-indigo-fetch-ikfast-plugin
Requires:       ros-indigo-fetch-maps
Requires:       ros-indigo-fetch-moveit-config
Requires:       ros-indigo-fetch-navigation
Requires:       ros-indigo-fetch-teleop
BuildRequires:  ros-indigo-catkin

%description
Fetch ROS, packages for working with Fetch and Freight

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
* Tue Mar 26 2019 Alex Moriarty <amoriarty@fetchrobotics.com> - 0.7.15-0
- Autogenerated by Bloom
