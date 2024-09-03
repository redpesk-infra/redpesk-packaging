Format: 1.0
Source: sec-gate-oidc
Binary: sec-gate-oidc, sec-gate-oidc-dev
Architecture: any
Version: 1.0.10
Maintainer: Valentin Lefebvre <valentin.lefebvre@iot.bzh>
Standards-Version: 3.8.2
Homepage: https://github.com/redpesk-common/sec-gate-oidc
Build-Depends: debhelper (>=5), 
    pkg-config,
    cmake,
    g++,
    sec-gate-fedid-binding-types-dev,
    libpam0g-dev,
    libpcsclite-dev,
    uthash-dev,
    libcurl4-gnutls-dev,
    linux-libc-dev,
    afb-cmake-modules,
    libjson-c-dev,
    afb-binding-dev,
    afb-libhelpers-dev,
    libafb-dev,
DEBTRANSFORM-RELEASE: 1

