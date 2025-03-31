Format: 1.0
Source: platform-info-binding
Binary: platform-info-binding-bin
Architecture: any
Version: 9.0.2
Maintainer: Valentin Lefebvre <valentin.lefebvre@iot.bzh>
Standards-Version: 3.8.2
Homepage: https://github.com/redpesk-common/platform-info-binding
Build-Depends: debhelper (>=5), 
    pkg-config,
    cmake, 
    g++,
    afb-binding-dev,
    libjson-c-dev,
    afb-libhelpers4-dev,
    librp-utils-json-c-dev,
    libudev-dev,
    platform-runtime-tools
DEBTRANSFORM-RELEASE: 1
