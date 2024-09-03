Format: 1.0
Source: sec-gate-fedid-binding
Binary: sec-gate-fedid-binding-bin, sec-gate-fedid-binding-dev
Architecture: any
Version: 1.0.6
Maintainer: Valentin Lefebvre <valentin.lefebvre@iot.bzh>
Standards-Version: 3.8.2
Homepage: https://github.com/redpesk-common/sec-gate-fedid-binding
Build-Depends: debhelper (>=5), 
    pkg-config,
    cmake,
    g++,
    linux-libc-dev,
    libsqlite3-dev,
    afb-cmake-modules,
    libjson-c-dev,
    libsystemd-dev (>= 222),
    afb-binding-dev,
    afb-libhelpers-dev,
DEBTRANSFORM-RELEASE: 1

