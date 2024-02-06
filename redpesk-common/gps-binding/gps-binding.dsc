Format: 1.0
Source:	gps-binding
Binary: gps-binding-bin, gps-binding-test
Architecture: any
Version: 1.1.2
Maintainer: Aymeric Aillet <aymeric.aillet@iot.bzh>
Standards-Version: 3.8.2
Homepage: http://git.ovh.iot/redpesk/redpesk-common/gps-binding.git
Build-Depends: debhelper (>= 5),pkg-config,
 cmake,
 afb-cmake-modules,
 g++,
 libsystemd-dev (>= 222),
 afb-binding-dev,
 libjson-c-dev,
 liblua5.3-dev,
 afb-libhelpers-dev,
 afb-libcontroller-dev,
 gpsd,
 gpsd-clients,
 libgps-dev,
 liburcu-dev,
DEBTRANSFORM-RELEASE: 1
Files:
 gps-binding-1.0.0.tar.gz
