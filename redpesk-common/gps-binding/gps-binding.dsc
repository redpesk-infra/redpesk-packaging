Format: 1.0
Source:	gps-binding
Binary: gps-binding-bin, gps-binding-test
Architecture: any
Version: 2.0.1
Maintainer: Aymeric Aillet <aymeric.aillet@iot.bzh>
Standards-Version: 3.8.2
Homepage: https://github.com/redpesk-common/gps-binding
Build-Depends: debhelper (>= 5),pkg-config,
 cmake,
 g++,
 afb-binding-dev,
 libjson-c-dev,
 afb-libhelpers4-dev,
 gpsd,
 gpsd-clients,
 libgps-dev,
 liburcu-dev,
DEBTRANSFORM-RELEASE: 1
Files:
 gps-binding-2.0.1.tar.gz
