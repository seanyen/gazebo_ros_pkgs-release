Name:           ros-hydro-gazebo-ros-control
Version:        2.3.6
Release:        0%{?dist}
Summary:        ROS gazebo_ros_control package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/gazebo_ros_control
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-control-toolbox
Requires:       ros-hydro-controller-manager
Requires:       ros-hydro-gazebo-ros
Requires:       ros-hydro-pluginlib
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-transmission-interface
Requires:       ros-hydro-urdf
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-control-toolbox
BuildRequires:  ros-hydro-controller-manager
BuildRequires:  ros-hydro-gazebo-ros
BuildRequires:  ros-hydro-joint-limits-interface
BuildRequires:  ros-hydro-pluginlib
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-transmission-interface
BuildRequires:  ros-hydro-urdf

%description
gazebo_ros_control

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Mon Aug 18 2014 Jonathan Bohren <jbo@jhu.edu> - 2.3.6-0
- Autogenerated by Bloom

