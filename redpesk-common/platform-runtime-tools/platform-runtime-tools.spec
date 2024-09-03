###########################################################################
# Copyright 2021 IoT.bzh
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
###########################################################################

#
# Specfile for Platform-duntime-tools
#

%global debug_package %{nil}
%global __os_install_post %{nil}
%define dracutlibdir %{_prefix}/lib/dracut


Name:       platform-runtime-tools
#Hexsha: 8612491b2a22c8325ac8dc264406fd3b0e1e1ad7
Version: 0.2.3
Release: 5%{?dist}
License:    GPL-3.0-only
Summary:    Platform info API for catch useful information about hardware/software
URL:        https://github.com/redpesk-common/platform-runtime-tools
Source0:    %{name}-%{version}.tar.gz
Source1:    20-%{name}.preset

BuildRequires: cmake
BuildRequires: gcc gcc-c++
BuildRequires: systemd-rpm-macros
BuildRequires: pkgconfig(libsystemd) >= 222

%ifarch	x86_64
Requires:      pciutils
%endif

Requires: systemd

BuildRoot:     %{_tmppath}/%{name}-%{version}-build

%description
Cmake project using script file and executable to save hard / soft informations during the first boot.
It also add services for systemd to run anytime and get informations in generated file.

%package -n dracut-%{name}
Summary:    Files %{name} for intallation using dracut
Provides:   %{name} = %{version}-%{release}
Requires:   platform-runtime-tools
Source10:   %{name}-module-setup.sh

%description -n dracut-%{name}
Add support of %{name} into redpesk recovery
(generated using dracut, to make initramfs and redpesk recovery)

%prep
%setup -q

%build
mkdir build && cd build
cmake -DCMAKE_INSTALL_BINDIR=%{_bindir} -DCMAKE_INSTALL_LIBDIR=%{_unitdir} ..
make

%install
cd build
make DESTDIR=%{buildroot} install
mkdir %{buildroot}%{_sysconfdir}/platform-info
mkdir -p /usr/lib/systemd/system-preset/

#preset systemd
%{__install} -d %{buildroot}%{_presetdir}
%{__install} -m 0644 %{SOURCE1} %{buildroot}%{_presetdir}

#dracut files
%{__install} -d %{buildroot}%{dracutlibdir}/modules.d/50platformtools
%{__install} -m 0755 %{SOURCE10} %{buildroot}%{dracutlibdir}/modules.d/50platformtools/module-setup.sh


%post
%systemd_post platform-core-detection.service
%systemd_post platform-os-detection.service
%systemd_post platform-devices-detection.service


%preun
%systemd_preun platform-core-detection.service
%systemd_preun platform-os-detection.service
%systemd_preun platform-devices-detection.service


%postun
%systemd_postun_with_restart platform-core-detection.service
%systemd_postun_with_restart platform-os-detection.service
%systemd_postun_with_restart platform-devices-detection.service


%files
%defattr(-,root,root)
%{_bindir}/pr-customize
%{_bindir}/pr-detect
%{_bindir}/pr-registry
%dir %{_sysconfdir}/pr-tools
%{_sysconfdir}/pr-tools/registry.conf
%{_sysconfdir}/pr-tools/registry.conf.d
%{_unitdir}/platform-core-customize.service
%{_unitdir}/platform-core-detection.service
%{_unitdir}/platform-devices-customize.service
%{_unitdir}/platform-devices-detection.service
%{_unitdir}/platform-os-customize.service
%{_unitdir}/platform-os-detection.service
%{_presetdir}/%{basename: %SOURCE1}
%dir /libexec
%dir /libexec/pr-tools
%dir /libexec/pr-tools/detect
%dir /libexec/pr-tools/detect/core
%dir /libexec/pr-tools/detect/devices
%dir /libexec/pr-tools/detect/os
%dir /libexec/pr-tools/customize
%dir /libexec/pr-tools/customize/core
%dir /libexec/pr-tools/customize/devices
%dir /libexec/pr-tools/customize/os
/libexec/pr-tools/detect/core/10_generic_hardware.sh
/libexec/pr-tools/detect/core/50_intel.sh
/libexec/pr-tools/detect/core/50_raspberry-pi.sh
/libexec/pr-tools/detect/core/50_renesas-rcar.sh
/libexec/pr-tools/detect/core/50_nitrogen.sh
/libexec/pr-tools/detect/core/50_solidrun.sh
/libexec/pr-tools/detect/devices/10_generic_device.sh
/libexec/pr-tools/detect/os/1_os_release.sh
%dir %{_sysconfdir}/platform-info

%files -n dracut-%{name}
%dir %{dracutlibdir}
%dir %{dracutlibdir}/modules.d
%dir %{dracutlibdir}/modules.d/50platformtools
%{dracutlibdir}/modules.d/50platformtools/module-setup.sh

%check

%clean
rm -rf build/*

%changelog
* Thu May 04 2023 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.2.3
- Upgrade version from source commit sha: 8612491b2a22c8325ac8dc264406fd3b0e1e1ad7
- Commit message:
- 	services: start AFTER / is mounted & if /etc is RW
- 	
- 	This is preferred to be sure that /etc/ will be mounted as RW FS even
- 	after a remount of fs !!
- 	On Read-Only FS, /etc may be not mounted as read/write. In this case,
- 	the service will not start as start condition failed.
- 	
- 	Signed-off-by: Pierre Marzin <pierre.marzin@iot.bzh>


* Tue Feb 28 2023 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.2.2
- Upgrade version from source commit sha: 4f4646abd420bca2567516858e0978d8f28df830
- Commit message:
- 	scriptlets: correct indent
- 	
- 	Signed-off-by: Pierre Marzin <pierre.marzin@iot.bzh>


* Mon Feb 27 2023 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.2.1
- Upgrade version from source commit sha: 5d68566106b1cc265947d8adee88141a2647a706
- Commit message:
- 	services: start AFTER systemd-modules-load
- 	
- 	This is preferred to be sure that /etc/ will be mounted as RW FS.
- 	Otherwise, data could not be written into output files if FS is
- 	not properly mounted yet.
- 	
- 	Signed-off-by: Pierre Marzin <pierre.marzin@iot.bzh>


* Fri Sep 24 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.2.0
- Upgrade version from source commit sha: 143b86da2008e49e072387adcc6a0920a014d0f8
- Commit message:
- 	Update OS name and os version
- 	
- 	Fix how to parse the /etc/os-relese to get the proper name and version
- 	for the os
- 	
- 	Signed-off-by: vlefebvre <valentin.lefebvre@iot.bzh>


* Tue Aug 24 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.1.0+20210824+2+g274f2ac
- Upgrade version from source commit sha: 274f2acae725e1e370ae12ead174360c45c21791
- Commit message:
- 	[Packaging] Fix installation service systemd path
- 	
- 	Signed-off-by: vlefebvre <valentin.lefebvre@iot.bzh>


* Mon Mar 29 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.1.0
- Upgrade version from source commit sha: 20b59356dbc64ef467d1b914c64821aab7a91486
- Commit message:
- 	remove function afm_packages_installed
- 	
- 	Signed-off-by: Valentin Lefebvre <valentin.lefebvre@iot.bzh>


* Tue Mar 23 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.0.0
- Upgrade version from source commit sha: 20b59356dbc64ef467d1b914c64821aab7a91486
- Commit message:
- 	remove function afm_packages_installed
- 	
- 	Signed-off-by: Valentin Lefebvre <valentin.lefebvre@iot.bzh>


* Wed Mar 10 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210310+134032+0+g9c96e1d1
- Upgrade version from source commit sha: 9c96e1d1ee1ea60bb403c25ac79ccfc2673da161
- Commit message:
- 	add os detection service
- 	
- 	Signed-off-by: Valentin Lefebvre <valentin.lefebvre@iot.bzh>


* Wed Mar 10 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210309+161347+0+g5327ccc1
- Upgrade version from source commit sha: 5327ccc18910eb31e1fb9436033f7da205ee3bda
- Commit message:
- 	add nitrogen adapation and OS informations
- 	
- 	Signed-off-by: Valentin Lefebvre <valentin.lefebvre@iot.bzh>


* Wed Mar 10 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20200304+112615+0+g42278912
- Upgrade version from source commit sha: 42278912c035966de03d91eb2960e45dfa6752b8
- Commit message:
- 	detect: core: renesas: Add GPU_FREQ key
- 	
- 	Read current GPU Frequency.
- 	
- 	Signed-off-by: Pierre Marzin <pierre.marzin@iot.bzh>
