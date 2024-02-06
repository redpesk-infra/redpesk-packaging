Name: spawn-binding
#Hexsha: 498162153e51482f96b86b8bc9033e0865f0442b
Version: 0.1.1+20220420+3+g4981621
Release: 6%{?dist}
Summary: %{name} support shell execution within a secured container with optional output formatting
Group:   Development/Libraries/C and C++
License:  Apache-2.0
URL: http://git.ovh.iot/redpesk/redpesk-common/spawn-binding
Source: %{name}-%{version}.tar.gz

%if 0%{?suse_version}
Patch: 00-suse-memfd.patch
%endif

BuildRequires:  afb-cmake-modules
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(afb-binding)
BuildRequires:  pkgconfig(afb-libhelpers)
BuildRequires:  pkgconfig(afb-libcontroller)
Requires:       afb-binder
BuildRequires:  afm-rpm-macros
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(libcap-ng)
BuildRequires:  uthash-devel

%description
%{name}

%afm_package

%afm_package_devel

%define afm_extra_files_devel \
%{_includedir}/*.h \
%{_libdir}/pkgconfig/*.pc

%prep
%autosetup -p 1

%build
%afm_configure_cmake
%afm_build_cmake

%install
%afm_makeinstall


%check

%clean

%changelog
* Mon Jul 05 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210705+8+ge237b62
- Upgrade version from source commit sha: e237b62bed6b679322c28118653d3f6623770fcc
- Commit message:
- 	Update config.cmake project info
- 	
- 	Signed-off-by: Pierre Marzin <pierre.marzin@iot.bzh>


* Mon Mar 08 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210308+135216+0+gcb3c3d37
- Upgrade version from source commit sha: cb3c3d37edcc1183e61d7f590c1621f15e08fa55
- Commit message:
- 	added Synchronous Encoder


* Tue Jan 26 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210126+164049+0+g4abfbbbe
- Upgrade version from source commit sha: 4abfbbbec8b3c8df5948b95cc368d14caa007288
- Commit message:
- 	fix pipe asynchronous flag


* Tue Jan 26 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210121+184443+0+g1693fbb2
- Upgrade version from source commit sha: 1693fbb2f479c97263671a8dfa075ee67f3ade7a
- Commit message:
- 	Added log format and updated documentation


* Wed Jan 20 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210120+093438+0+g212ec2eb
- Upgrade version from source commit sha: 212ec2eb0c6e06e9b893aa953eb971d33ab271ed
- Commit message:
- 	Fix warnings
-
- 	Signed-off-by: Corentin LE GALL <corentin.legall@iot.bzh>


* Wed Jan 20 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210119+190746+0+gd61b4d86
- Upgrade version from source commit sha: d61b4d86b973bc64fff270d728a29922c70ee3b5
- Commit message:
- 	Update simple config add buffer fix to json encoder


* Tue Jan 19 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210119+134038+0+gacef3479
- Upgrade version from source commit sha: acef3479935b309ff96cf610a1296bd9b849b026
- Commit message:
- 	update optionnal argument
- 	Merge branch 'master' of git.ovh.iot:redpesk/redpesk-common/spawn-binding


* Mon Jan 18 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210118+154829+0+g52cf45c9
- Upgrade version from source commit sha: 52cf45c98da7a6d77ec772f3965d27727adf98b1
- Commit message:
- 	Fix double free on timeout verb
-
- 	Signed-off-by: Corentin LE GALL <corentin.legall@iot.bzh>


* Mon Jan 18 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210117+111505+0+g85d9f983
- Upgrade version from source commit sha: 85d9f983a0b717e2d8cf8210dd6486ef739b6927
- Commit message:
- 	Documentation updates


* Thu Jan 14 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210114+165706+0+gea176366
- Upgrade version from source commit sha: ea176366ffbf9ebd368f4648e24caa8fc793b937
- Commit message:
- 	move sample in doc from simple to sandbox


* Thu Jan 14 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210114+132213+0+g67767bac
- Upgrade version from source commit sha: 67767bac0d9e1ade679f3b336077304e53bf0b97
- Commit message:
- 	README.md: fix typos


* Wed Jan 13 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210113+005317+0+g579cedd6
- Upgrade version from source commit sha: 579cedd6e61aacb2f431e9e26f67442816f088c3
- Commit message:
- 	c++


* Wed Jan 13 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210113+005317+0+g579cedd6
- Upgrade version from source commit sha: 579cedd6e61aacb2f431e9e26f67442816f088c3
- Commit message:
- 	c++


* Tue Jan 12 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210112+170106+0+g99c5e967
- Upgrade version from source commit sha: 99c5e967db9b43584038da32640d985d83e5acba
- Commit message:
- 	[Cmake] remove project() function
-
- 	It was overriding project variables to empty.
-
- 	Signed-off-by: Corentin LE GALL <corentin.legall@iot.bzh>



* Tue Jan 12 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210112+150730+0+g8ed29fff
- Upgrade version from source commit sha: 8ed29fffe2597372bf2d400014be34303bb4c7a0
- Commit message:
- 	Fix warnings and errors
-
- 	Signed-off-by: Corentin LE GALL <corentin.legall@iot.bzh>

