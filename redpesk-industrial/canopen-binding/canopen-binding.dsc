Format: 1.0
Source: canopen-binding
Binary: canopen-binding-test, canopen-binding-dev, canopen-binding-bin
Architecture: any
Version: 0.0.0
Maintainer: unknown <corentin@unknown>
Homepage: https://git.ovh.iot/redpesk/redpesk-industrial/canopen-binding
Standards-Version: 4.4.1
Build-Depends: debhelper-compat (= 12),debhelper (>= 5),pkg-config,	
 cmake,
 afb-cmake-modules,
 g++, 
 libsystemd-dev (>= 222),
 afb-binding-dev,
 libjson-c-dev,
 liblua5.3-dev,
 afb-libhelpers-dev,
 afb-libcontroller-dev,
 liblely-coapp2,
 liblely-dev
Package-List:
 canopen-binding-bin deb libs optional arch=any
 canopen-binding-dev deb libdevel optional arch=any
 canopen-binding-test deb libdevel optional arch=any
Files:
 canopen-binding-0.0.0.tar.gz
DEBTRANSFORM-RELEASE: 1