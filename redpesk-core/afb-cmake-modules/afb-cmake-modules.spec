Name:           afb-cmake-modules
# WARNING {name} is not used for tar file name in source nor for setup
#         Check hard coded values required to match git directory naming
BuildArchitectures: noarch
#Hexsha: 63451c5868b5dce02229bf9eb253b3f42197f565
Version: 10.0.9
Release: 7%{?dist}
License:        Apache-2.0
Summary:        afb-cmake-modules
Group:          Development/Libraries/C and C++
Url:            https://github.com/redpesk-core/afb-cmake-modules
Source:         %{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
Requires:       afb-idl
Requires:       zip

%description
This is a CMake module made to ease development of binding and application
framework binder apps.

%prep
%autosetup -p1

%build
[ ! -d build ] && mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_INSTALL_LIBDIR=%{_lib} ..

%install
[ -d build ] && cd build
%make_install

%files
%defattr(-,root,root)
%dir %{_datadir}/cmake/Modules/
%dir %{_datadir}/doc/CMakeAfbTemplates/
%{_datadir}/cmake/Modules/*
%{_datadir}/pkgconfig/cmake_afb_templates.pc
%{_datadir}/doc/CMakeAfbTemplates/*
%{_datadir}/pkgconfig/cmake_afb_templates.pc

%changelog

* Fri Jan 20 2023 José Bollo jose.bollo@iot.bzh 10.0.5+23+g8d2e276
Bump to Version 10.0.6

* Thu Jan 12 2023 José Bollo jose.bollo@iot.bzh 10.0.5
Bump to Version 10.0.5
* Fri Oct 01 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 10.0.4
- Upgrade version from source commit sha: d86cd5ad06acfc8cf938eb82ce40426f2f3d7f1d
- Commit message:
- 	add the 'info_verb_generate' macro
-
- 	Add this macro to generate the info_verb.c from an existing
- 	info_verb.json file, in the calling project source directory.
-
- 	Added a pkg-config file in order to add the dependency to
- 	projects that need it.
-
- 	Signed-off-by: Thierry Bultel <thierry.bultel@iot.bzh>


* Mon Jun 07 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 10.0.3
- Upgrade version from source commit sha: 65ccf532ec06cdf44f4cbc3e80d073f545f280ab
- Commit message:
- 	Bug afb-client in launcher
-
- 	Signed-off-by: Arthur Guyader <arthur.guyader@iot.bzh>
- 	Change-Id: I1e135a3ef0491f03b7e8be72098e6f4c2de795f4


* Fri Jun 04 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 10.0.2
- Upgrade version from source commit sha: d323d5729140718b012e3d4aee904d5d467430bb
- Commit message:
- 	Remove useless code in test launcher
-
- 	Signed-off-by: Arthur Guyader <arthur.guyader@iot.bzh>
- 	Change-Id: Ie08c7b20109e59dab3b20c5a49dde08c27735ec4


* Thu Jun 03 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 10.0.1
- Upgrade version from source commit sha: dafe58f906651be4ac919a33eb9a797b6843be05
- Commit message:
- 	Change permissions :test => ::partner:launch-afbtest
-
- 	Signed-off-by: Arthur Guyader <arthur.guyader@iot.bzh>
- 	Change-Id: I1a327f3e72a1dfe25f96c9f6014d0a79f08e3225


* Fri Dec 11 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 10.0.0
- Upgrade version from source commit sha: 0546ea29e69bc7923031c5bd5f984681274ae002
- Commit message:
- 	Merge branch 'sandbox/armand/fix-test-binding' into 'master'
-
- 	Change afb-client-demo to afb-client in launcher
-
- 	See merge request redpesk/redpesk-core/afb-cmake-modules!3


* Thu Nov 26 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.1+20201113+12+g4f9ae63
- Upgrade version from source commit sha: 4f9ae63a1399cdb5d682725368c9679a4e6d975d
- Commit message:
- 	Fix a warning
-
- 	Before the change the following warning was issued:
-
- 	  CMake Warning (dev) in .../CMakeAfbTemplates/cmake/cmake.d/01-build_options.cmake:
- 	    A logical block opening on the line
-
- 	      .../CMakeAfbTemplates/cmake/cmake.d/01-build_options.cmake:153 (IF)
-
- 	    closes on the line
-
- 	      .../CMakeAfbTemplates/cmake/cmake.d/01-build_options.cmake:155 (ENDIF)
-
- 	    with mis-matching arguments.


* Mon Nov 16 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.1+20201113+12+g4f9ae63
- Upgrade version from source commit sha: 4f9ae63a1399cdb5d682725368c9679a4e6d975d
- Commit message:
- 	Fix a warning
-
- 	Before the change the following warning was issued:
-
- 	  CMake Warning (dev) in .../CMakeAfbTemplates/cmake/cmake.d/01-build_options.cmake:
- 	    A logical block opening on the line
-
- 	      .../CMakeAfbTemplates/cmake/cmake.d/01-build_options.cmake:153 (IF)
-
- 	    closes on the line
-
- 	      .../CMakeAfbTemplates/cmake/cmake.d/01-build_options.cmake:155 (ENDIF)
-
- 	    with mis-matching arguments.


* Wed Dec 12 2018 Romain Forlot <claneys@iot.bzh> - 8.99.4
- Separation of docs files at installation
- Fix the install prefix at build time

* Thu Nov 05 2018 Romain Forlot <claneys@iot.bzh> - 6.90
- initial creation
