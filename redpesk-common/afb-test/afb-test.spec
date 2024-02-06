#
# spec file for package app-afb-test
#
Name:           afb-test
#Hexsha: 3832e4c24da0df4d8e5da44e6be54d846e59327e
Version: 10.1
Release:        29%{?dist}
License:        Apache-2.0
Summary:        afb-test
Group:          Development/Libraries/C and C++
URL:            https://git.ovh.iot/redpesk/redpesk-core/afb-test
Source:         %{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(lua) >= 5.3
BuildRequires:  cmake
BuildRequires:  afm-rpm-macros
BuildRequires:  afb-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(afb-binding)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(afb-libcontroller)
BuildRequires:  pkgconfig(afb-libhelpers)
BuildRequires:  pkgconfig(libsystemd) >= 222
Requires:       jq

%description
afb-test is a test framework made to test other binding.

# append afm-test in files
%define afm_extra_systemfiles \
	%{_bindir}/afm-test \
	%{nil}

#redefine afm_files_devel, no include files
%define afm_files_devel \
%{_libdir}/pkgconfig/*.pc \
%{nil}

%afm_package
%{_bindir}/afm-test

%define afm_files_devel \
%{_libdir}/pkgconfig/*.pc \
%{nil}

%afm_package_devel

%afm_package_test

%prep
%autosetup -p 1

sed -Ei 's/\$\{CMAKE_INSTALL_BINDIR\}/\/usr\/bin/gm;' afm-test.cmake
sed -Ei 's/cmake_minimum_required/CMAKE_MINIMUM_REQUIRED/gm;' CMakeLists.txt
sed -Ei 's/\$\{CMAKE_INSTALL_PREFIX\}\/redpesk/\$\{CMAKE_INSTALL_PREFIX\}/gm;' conf.d/cmake/config.cmake

%build
%afm_configure_cmake \
%if 0%{?redpesk_ver}
    -DONTARGET=YES
%endif

%afm_build_cmake

%install
%afm_makeinstall

%check

%clean

%changelog
* Thu Dec 17 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.1+20201217+41+g4dfa9c0
- Upgrade version from source commit sha: 4dfa9c0e2a0ffeb4da816106769b07c606578040
- Commit message:
- 	afb-test.pc: Change afb-binder to afb-binding
-
- 	Signed-off-by: Corentin LE GALL <corentin.legall@iot.bzh>


* Tue Dec 15 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.1+20201214+32+gec7359e
- Upgrade version from source commit sha: ec7359edd2d5237e2551c8568860a6cfb5979055
- Commit message:
- 	Correction of afm-test script in native environment
-
- 	- Change afb-daemon to afb-binder
- 	- Change path to aft.so
- 	- Delete "--token" flag
-
- 	Signed-off-by: Armand BENETEAU <armand.beneteau@iot.bzh>


* Mon Dec 07 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.1+20201207+31+g092d8f8
- Upgrade version from source commit sha: 092d8f87b1e0b7a502419c2f5a55fa7dba57936e
- Commit message:
- 	conf.cmake: Rename cmake dependencies
-
- 	Signed-off-by: Corentin LE GALL <corentin.legall@iot.bzh>


* Mon Aug 24 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.1+20200728+16+g7328dec
- Upgrade version from source commit sha: 7328dec70e8e00e01b7e0308c41f8b51d93e81da
- Commit message:
- 	Fix indentation problem
-
- 	Fix an indentation problem on the new coverage reports feature
-
- 	Signed-off-by: Aymeric Aillet <aymeric.aillet@iot.bzh>



* Wed May 27 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.0.3+4+g48229b99
- Upgrade version from source commit sha: 48229b99d630ba621cb71eae233f589a0240beec
- Commit message:
- 	Remove dirty fix and simplify waiting while loop
-
- 	Fix has been made on appfw main, so now use it and remove the dirty fix
-
- 	Change-Id: I8d54ba6fb8f7a0d1121bd30969cd4567e4d117dd
- 	Signed-off-by: Romain Forlot <romain.forlot@iot.bzh>


* Wed May 27 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> g48229b99
- Upgrade version from source commit sha: 48229b99d630ba621cb71eae233f589a0240beec
- Commit message:
- 	Remove dirty fix and simplify waiting while loop
-
- 	Fix has been made on appfw main, so now use it and remove the dirty fix
-
- 	Change-Id: I8d54ba6fb8f7a0d1121bd30969cd4567e4d117dd
- 	Signed-off-by: Romain Forlot <romain.forlot@iot.bzh>


* Wed May 27 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.0.3+3+gcc7b3b8e
- Upgrade version from source commit sha: cc7b3b8ea7c959aae31505a58522164f636fb5ba
- Commit message:
- 	Fix waiting process end watching resulting files
-
- 	Quick and dirty fix waiting for a fix on appfw main to correctly get
- 	the pid and waiting on it instead of the resulting files.
-
- 	Change-Id: I5f32e00e372fba933581ec7b9fe517704582cbc9
- 	Signed-off-by: Romain Forlot <romain.forlot@iot.bzh>


* Wed May 27 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> gcc7b3b8e
- Upgrade version from source commit sha: cc7b3b8ea7c959aae31505a58522164f636fb5ba
- Commit message:
- 	Fix waiting process end watching resulting files
-
- 	Quick and dirty fix waiting for a fix on appfw main to correctly get
- 	the pid and waiting on it instead of the resulting files.
-
- 	Change-Id: I5f32e00e372fba933581ec7b9fe517704582cbc9
- 	Signed-off-by: Romain Forlot <romain.forlot@iot.bzh>


* Tue May 26 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.0.3+2+gaae9c2cb
- Upgrade version from source commit sha: aae9c2cb23111ed37cb412e86c84c13b0d690879
- Commit message:
- 	Merge branch 'sandbox/clement/afm-test-binding-id' into 'master'
-
- 	afm-test.target: allow to give the agl binding id
-
- 	See merge request iotbzh/app-afb-test!1


* Tue May 19 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.0.3+2+gaae9c2cb
- Upgrade version from source commit sha: aae9c2cb23111ed37cb412e86c84c13b0d690879
- Commit message:
- 	Merge branch 'sandbox/clement/afm-test-binding-id' into 'master'
-
- 	afm-test.target: allow to give the agl binding id
-
- 	See merge request iotbzh/app-afb-test!1


* Thu Mar 26 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.0.3
- Upgrade version from source commit sha: 6d88f0e1cce0b0da581c210cc515844e3abf2099
- Commit message:
- 	afm-test: Fix "Resource temporarily unavailable"
-
- 	This fiw the error message:
- 	"failed Resource temporarily unavailable"
- 	when using afm-test on a target. This is because the wgt already died and so the
- 	afb-util tool can't kill it again ^^
-
- 	Change-Id: I826ccaf599d8d1b5f2e2cbc94c0226ada23ac7bc
- 	Signed-off-by: Romain Forlot <romain.forlot@iot.bzh>


* Thu Mar 26 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.0.2
- Upgrade version from source commit sha: 647bae158d6adfcc55bdc0186ff08480d399c698
- Commit message:
- 	aft: Fix failure on skipped test
-
- 	aft: Fix failure on skipped test because wrong parameters value.
- 	This adds checks on function parameters to get it output a right
- 	failure message.
-
- 	Change-Id: I9f2e4ac56294bc4e64bf3377b3dbe09ca2c8adea
- 	Signed-off-by: Romain Forlot <romain.forlot@iot.bzh>


* Thu Mar 26 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.0.1
- Upgrade version from source commit sha: 58c9922bab4a0c11142633dfe4522f993e97178d
- Commit message:
- 	afm-test: fix app home directory to /home/$(id -u)
-
- 	Change-Id: Iade89c31a92f74bf32fa178d613959c4660144de
- 	Signed-off-by: Romain Forlot <romain.forlot@iot.bzh>


* Wed Mar 25 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 8.99.5+5+gfd875471
- Upgrade version from source commit sha: fd875471f19f66f79904694e166ef481f6b2e591
- Commit message:
- 	Change project to make it all coherent.
-
- 	Change-Id: If86c815c469b711bcf748244f215110a5adb648b
- 	Signed-off-by: Romain Forlot <romain.forlot@iot.bzh>


* Wed Mar 25 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 8.99.5+4+gfa1239ca
- Upgrade version from source commit sha: fa1239ca2274c8dc51d0dc02a13fcd6549dfbcd8
- Commit message:
- 	Fix signal 11 segfault in pthread
-
- 	This fix a segfault happening using systemd service where the the end of test from the
- 	binder point of view is done but the test are running. This was because the binding answer
- 	to the binder's request at the beginning of the test instead of the end.
-
- 	This commit adds also useful details in the request answer
-
- 	Change-Id: I8dd5b0e7a61608d3b7736ed278d92376f0d11fd3
- 	Signed-off-by: Romain Forlot <romain.forlot@iot.bzh>

* Thu Nov 7 2019 Armand B.
- Modification for RedPesk integration

* Thu Oct 25 2018 Romain
- initial creation


