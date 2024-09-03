Format: 1.0
Source: platform-info-binding
Binary: platform-info-binding-bin
Architecture: any
Version: 1.0-list
Maintainer: Valentin Lefebvre <valentin.lefebvre@iot.bzh>
Standards-Version: 3.8.2
Homepage: https://github.com/redpesk-common/platform-info-binding
Build-Depends: debhelper (>=5), 
    pkg-config,
    cmake, 
    g++,
    afb-cmake-modules,
    rp-libmicrohttpd-dev | libmicrohttpd-dev,
    libsystemd-dev (>= 222),
    afb-binding-dev,
    libjson-c-dev,
    afb-libhelpers-dev,
    platform-runtime-tools
DEBTRANSFORM-RELEASE: 1
