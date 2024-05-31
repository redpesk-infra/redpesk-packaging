Format: 1.0
Source: canopen-binding
Binary: canopen-binding-dev, canopen-binding-bin
Architecture: any
Version: 2.0.2
Maintainer: unknown <corentin@unknown>
Homepage: https://git.ovh.iot/redpesk/redpesk-industrial/canopen-binding
Standards-Version: 4.4.1
Build-Depends:
 debhelper-compat (= 12),
 debhelper (>= 5),
 pkg-config,	
 cmake,
 g++, 
 afb-binding-dev,
 libjson-c-dev,
 afb-libhelpers4-static,
 librp-utils-static,
 liblely-coapp-dev
Package-List:
 canopen-binding-bin deb libs optional arch=any
 canopen-binding-dev deb libdevel optional arch=any
Files:
 canopen-binding-2.0.2.tar.gz
DEBTRANSFORM-RELEASE: 1
