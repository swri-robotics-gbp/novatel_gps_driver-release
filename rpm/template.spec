Name:           ros-lunar-novatel-gps-driver
Version:        3.3.0
Release:        0%{?dist}
Summary:        ROS novatel_gps_driver package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       libpcap-devel
Requires:       ros-lunar-diagnostic-msgs
Requires:       ros-lunar-diagnostic-updater
Requires:       ros-lunar-gps-common
Requires:       ros-lunar-nav-msgs
Requires:       ros-lunar-nodelet
Requires:       ros-lunar-novatel-gps-msgs
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-sensor-msgs
Requires:       ros-lunar-std-msgs
Requires:       ros-lunar-swri-math-util
Requires:       ros-lunar-swri-nodelet
Requires:       ros-lunar-swri-roscpp
Requires:       ros-lunar-swri-serial-util
Requires:       ros-lunar-swri-string-util
Requires:       ros-lunar-tf
BuildRequires:  boost-devel
BuildRequires:  libpcap-devel
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-diagnostic-msgs
BuildRequires:  ros-lunar-diagnostic-updater
BuildRequires:  ros-lunar-gps-common
BuildRequires:  ros-lunar-nav-msgs
BuildRequires:  ros-lunar-nodelet
BuildRequires:  ros-lunar-novatel-gps-msgs
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-sensor-msgs
BuildRequires:  ros-lunar-std-msgs
BuildRequires:  ros-lunar-swri-math-util
BuildRequires:  ros-lunar-swri-nodelet
BuildRequires:  ros-lunar-swri-roscpp
BuildRequires:  ros-lunar-swri-serial-util
BuildRequires:  ros-lunar-swri-string-util
BuildRequires:  ros-lunar-tf

%description
Driver for NovAtel receivers

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Thu Aug 31 2017 P. J. Reed <preed@swri.org> - 3.3.0-0
- Autogenerated by Bloom

