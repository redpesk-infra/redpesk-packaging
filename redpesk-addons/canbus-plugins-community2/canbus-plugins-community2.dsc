Format: 1.0
Source: canbus-plugins-community
Binary: canbus-plugins2-obd2,
        canbus-plugins2-hvac,
        canbus-plugins2-vcar,
        canbus-plugins2-engine
Architecture: any
Version: 2.0.2
Maintainer: unknown <unknown@debian.org>
Standards-Version: 3.8.2
Homepage: http://git.ovh.iot/redpesk/redpesk-common/community-can-low-level-plugins.git
Build-Depends: debhelper (>= 5),pkg-config,
 cmake (>= 3.10),
 g++,
 afb-binding-dev,
 canbus-binding-dev (>= 2),
 canbus-generator-bin (>= 2)
DEBTRANSFORM-RELEASE: 1
Files:
 canbus-plugins-community2-2.0.2.tar.gz
