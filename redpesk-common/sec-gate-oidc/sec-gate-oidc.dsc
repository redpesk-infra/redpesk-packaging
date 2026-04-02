Format: 1.0
Source: sec-gate-oidc
Binary: sec-gate-oidc, sec-gate-oidc-dev
Architecture: any
Version: 2.0.0
Maintainer: Valentin Lefebvre <valentin.lefebvre@iot.bzh>
Standards-Version: 3.8.2
Homepage: https://github.com/redpesk-common/sec-gate-oidc
Build-Depends: debhelper (>=5), 
    pkg-config,
    cmake,
    gcc,
    sec-gate-fedid-binding-types-dev,
    libpam0g-dev,
    libpcsclite-dev,
    libcurl4-gnutls-dev,
    uthash-dev,
    libjson-c-dev,
    libafb-dev,
    librp-utils-core-dev,
    librp-utils-json-c-dev,
DEBTRANSFORM-RELEASE: 1

