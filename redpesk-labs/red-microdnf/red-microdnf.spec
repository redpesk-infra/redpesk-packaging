Name:           red-microdnf
#Hexsha: c5ca70eb087d6bd18cf195e277fe018a282f9dfb
Version: 1.0.1
Release: 5%{?dist}
Summary:        red-microdnf: for of microdnf
License:        LGPLv2.1+
URL:			http://git.ovh.iot/redpesk/redpesk-labs/red-microdnf.git
Source:         %{name}-%{version}.tar.gz
BuildRequires:	red-pak-devel
BuildRequires:	libdnf5-devel
BuildRequires:  libassuan-devel
BuildRequires:	libdnf5-cli-devel
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  pkgconfig(uuid)

Requires:		libdnf5
Requires:		libdnf5-cli
Requires:		red-pak

%description
%{summary}.

%prep
%autosetup -p 1

%build
%cmake
%cmake_build

%install
%cmake_install


%files
%defattr(-,root,root)
%{_bindir}/redmicrodnf
%{_sysconfdir}/bash_completion.d/redmicrodnf


%changelog
* Wed Dec 01 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20211201+124320+0+gf20320b
- Upgrade version from source commit sha: f20320b7f8f8b249c36a895f62ebad22d7904b28
- Commit message:
- 	install: feature toinstall rpm file directly
-
- 	Signed-off-by: Clement Benier <clement.benier@iot.bzh>


* Wed Dec 01 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20211130+102951+0+g76e142b
- Upgrade version from source commit sha: 76e142b91194a5720cc63296cc6f22255e65627b
- Commit message:
- 	main: fix global_option to redlib
-
- 	Signed-off-by: Clement Benier <clement.benier@iot.bzh>


* Tue Aug 24 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210824+095058+0+g792e4cd
- Upgrade version from source commit sha: 792e4cd2110511494ecc6c11077bb6767edc9dd0
- Commit message:
- 	rednode: all commands
-
- 	Signed-off-by: Clement Benier <clement.benier@iot.bzh>


* Tue Jul 27 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210727+173702+0+g024c4f0
- Upgrade version from source commit sha: 024c4f04bf0885574c29a08ea8f818a00daa6886
- Commit message:
- 	main: add manager command

- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


* Tue Jul 27 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210727+170836+0+gf7250d9
- Upgrade version from source commit sha: f7250d9fde6249da2d33e057cb6775716a243995
- Commit message:
- 	CMakeLists: sources files
-
- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


* Tue Jul 27 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210727+165330+0+g350ec8d
- Upgrade version from source commit sha: 350ec8d73d0206818b983f3907c30136b0607ae4
- Commit message:
- 	CMakeLists: libdnf librairies
-
- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


* Tue Jul 27 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210727+151313+0+g72e8830
- Upgrade version from source commit sha: 72e8830423cf58b82dcb8a88ed2a6b9953fc3ff8
- Commit message:
- 	manager: no redpath
-
- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


* Tue Jul 27 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210727+150229+0+g15c5b6c
- Upgrade version from source commit sha: 15c5b6cbb9579d8a4e6a78a1917f30a90fee1c0f
- Commit message:
- 	CMakeLists: libs+add_definition
-
- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


* Tue Jul 27 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210727+122101+0+g7f851c2
- Upgrade version from source commit sha: 7f851c26803e40e0468d20017731b9080a4995ff
- Commit message:
- 	CMakeLists: cxx17
-
- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


* Tue Jul 27 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210727+121246+0+g04edc28
- Upgrade version from source commit sha: 04edc28bfd20753bc8144a5b8dca18223c9fdb28
- Commit message:
- 	CMakeLists: include_directories
-
- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


* Tue Jul 27 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210727+113657+0+g9bdc2e7
- Upgrade version from source commit sha: 9bdc2e70b9b1d9d15c0f8496b6ff3c17c94036ae
- Commit message:
- 	CMakeLists: include_directories
-
- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


* Tue Jul 27 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210727+105008+0+g052d10f
- Upgrade version from source commit sha: 052d10f9385014a8d648825413a64038622aca36
- Commit message:
- 	CMakeLists: cmake_minimum_required + project()
-
- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


* Tue Jul 27 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210727+101940+0+ge643f8a
- Upgrade version from source commit sha: e643f8a6daf30f978ade7100608ec21fc8954736
- Commit message:
- 	CMakeLists: find_package(PkgConfig REQUIRED)
-
- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


* Mon Jul 26 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210726+113747+0+g996d8c4
- Upgrade version from source commit sha: 996d8c4eb0972f1caf427cb91999b7d9e7b6a4ea
- Commit message:
- 	rebase patch
-
- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


* Mon Jul 26 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210726+113747+0+g996d8c4
- Upgrade version from source commit sha: 996d8c4eb0972f1caf427cb91999b7d9e7b6a4ea
- Commit message:
- 	rebase patch
-
- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


