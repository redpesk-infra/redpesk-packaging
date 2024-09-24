Format: 1.0
Source: afb-libafb
Binary: libafb6, libafbcli6
Architecture: any
Version: 5.3.1
Maintainer: José Bollo <jose.bollo@iot.bzh>
Standards-Version: 3.8.2
Homepage: https://github.com/redpesk-core/afb-libafb
Build-Depends:
 debhelper (>= 5),
 dpkg-dev,
 pkg-config,	
 cmake,
 libmicrohttpd-dev (>= 0.9.60),
 libsystemd-dev (>= 222),
 libssl-dev,
 libgcrypt20-dev,
 libjson-c-dev,
 librp-utils-dev (>= 0.0.4),
 libmagic-dev,
 gnutls-dev,
 afb-binding-dev (>= 4.1.2)
Files:
 afb-libafb-5.3.1.tar.gz
DEBTRANSFORM-RELEASE: 1
