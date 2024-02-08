%define secname sec-lsm-manager

Name:           sec-lsm-manager
#Hexsha: d8e176e8edcc3cebe5d995f538dcb287eb3ff890
Version: 2.6.1
Release: 47%{?dist}
Summary:        sec-lsm-manager service (SMACK, SELinux)
License:        Apache-2.0
URL:            https://github.com/redpesk-core/sec-lsm-manager
Source:         %{name}-%{version}.tar.gz
BuildRequires:  m4
BuildRequires:  cmake
BuildRequires:  check-devel
BuildRequires:  gcc-c++
BuildRequires:  libcap-devel
BuildRequires:  pkgconfig(libsystemd) >= 222
BuildRequires:  pkgconfig(libsmack)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libsemanage)
BuildRequires:  pkgconfig(cynagora)
Requires(pre):  shadow-utils
Requires:       (%{name}-smack = %{version} or %{name}-selinux = %{version})

%description
%{summary}.

%package tool
Summary:        Tiny tool for %{name}
Requires:       %{name} = %{version}
Provides:       pkgconfig(%{name}) = %{version}

%description tool
%{summary}.

%package devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name} = %{version}
Provides:       pkgconfig(%{name}) = %{version}

%description devel
%{summary}.

%package selinux
Summary:        sec-lsm-manager service for SELinux
Requires:       %{name} = %{version}
Requires:       selinux-policy
Requires:       selinux-policy-devel
Provides:       %{name}-selinux = %{version}


%description selinux
%{summary}.

%package smack
Summary:        sec-lsm-manager service for SMACK
Requires:       %{name} = %{version}
Requires:       libsmack-userspace
Requires:       sec-smack-rules
Provides:       %{name}-smack = %{version}

%description smack
%{summary}.

%package selinux-redtest
Summary:        Test package of sec-lsm-manager service for SELinux
Requires:       %{name}-selinux = %{version}
Requires:       check
Provides:       %{name}-selinux-redtest = %{version}


%description selinux-redtest
%{summary}.

%package smack-redtest
Summary:        Test package of sec-lsm-manager service for SMACK
Requires:       %{name}-smack = %{version}
Requires:       check
Provides:       %{name}-smack-redtest = %{version}

%description smack-redtest
%{summary}.


%prep
%autosetup -p 1

%build
%cmake -DSYSTEMD_UNIT_DIR=/usr/lib/systemd/system  -DWITH_SYSTEMD=ON -DWITH_SMACK=ON -DWITH_SELINUX=ON .
%cmake_build

%install
%cmake_install
chmod o-x %{buildroot}%{_bindir}/sec-lsm-manager-cmd
mkdir -p %{buildroot}%{_prefix}/lib/%{name}-selinux-redtest/redtest
mkdir -p %{buildroot}%{_prefix}/lib/%{name}-smack-redtest/redtest
mv %{buildroot}/%{_datadir}/%{secname}/tests/tests-selinux %{buildroot}%{_prefix}/lib/%{name}-selinux-redtest/redtest/
mv %{buildroot}/%{_datadir}/%{secname}/tests/tests-smack %{buildroot}%{_prefix}/lib/%{name}-smack-redtest/redtest/
cp src/tests/run-redtest %{buildroot}%{_prefix}/lib/%{name}-selinux-redtest/redtest/
cp src/tests/run-redtest %{buildroot}%{_prefix}/lib/%{name}-smack-redtest/redtest/

%pre
getent group %{secname} >/dev/null || groupadd -r %{secname} ||:
getent passwd %{secname} >/dev/null || useradd --system --home %{_localstatedir}/lib/empty --no-create-home --shell /bin/false --gid %{secname} %{secname} || :

%files
%defattr(-,root,root)
%{_unitdir}
%{_unitdir}/sockets.target.wants
%{_bindir}/sec-lsm-managerd

%files tool
%defattr(-,root,root)
%{_bindir}/sec-lsm-manager-cmd

%files selinux
%defattr(-,root,root)
%{_bindir}/sec-lsm-manager-selinuxd
%defattr(-,%{secname},%{secname})
%{_datadir}/%{secname}/app-template.te
%{_datadir}/%{secname}/app-template.if
%{_datadir}/%{secname}/script
%{_datadir}/%{secname}/selinux-rules

%files smack
%defattr(-,root,root)
%{_bindir}/sec-lsm-manager-smackd
%defattr(-,%{secname},%{secname})
%{_datadir}/%{secname}/app-template.smack

%files devel
%{_includedir}/%{secname}.h
%{_libdir}/lib%{secname}*.a
%{_libdir}/pkgconfig/%{secname}.pc


%files selinux-redtest
%defattr(755,root,root)
%{_prefix}/lib/%{name}-selinux-redtest/redtest/*

%files smack-redtest
%defattr(755,root,root)
%{_prefix}/lib/%{name}-smack-redtest/redtest/*


%changelog

* Thu Nov 02 2023 José Bollo jose.bollo@iot.bzh 2.4.1
- extract sec-lsm-manager-cmd in seperate package

* Fri Jun 09 2023 José Bollo jose.bollo@iot.bzh 2.3.0
- replace smack-rules by sec-smack-rules

* Thu Jul 01 2021 José Bollo jose.bollo@iot.bzh 2.2.1
- Version 2.2.1

* Tue Jun 29 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 2.2.0+20210629+1+g59705ce
- Upgrade version from source commit sha: 59705cee636e4ae8b420eec1040fa0ed1de5936b
- Commit message:
- 	[bug] Patch tests with new public label
-
- 	Signed-off-by: Arthur Guyader <arthur.guyader@iot.bzh>
- 	Change-Id: I7317a3b7f6333cfbec71601e67b1fc6175c8062a


* Wed Jun 16 2021 Jose Bollo jose.bollo@iot.bzh 2.2.0
- Version 2.2.0
* Thu Jun 10 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 2.1.8
- Upgrade version from source commit sha: 2cf23689d5673ef080af4863c0d887115f3cd04c
- Commit message:
- 	[template] Update selinux and smack rules
-
- 	Signed-off-by: Arthur Guyader <arthur.guyader@iot.bzh>
- 	Change-Id: I86772126a7677ef01007b7b8a0afa4371edc1980


* Mon Jun 07 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 2.1.7
- Upgrade version from source commit sha: 60bbefb48b84a33e2faf8a3715ab28a82b9b7d85
- Commit message:
- 	[selinux] Add permissions and access setpgid
-
- 	- execute shell
- 	- access tmp
- 	- connect other binding
-
- 	Signed-off-by: Arthur Guyader <arthur.guyader@iot.bzh>
- 	Change-Id: I06232cdf8ccd08dfeef0d74b2f5ea10f2866ada9


* Thu Jun 03 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 2.1.6
- Upgrade version from source commit sha: 3eb2a4faefe62e5eb4fdfde3d55c844d9818ae3f
- Commit message:
- 	[selinux] Create attribute and allow rights on redpesk_public
-
- 	- Attribute contains all type
- 	- Some right on redpesk_public
- 	- Create perm to launch tests
-
- 	Signed-off-by: Arthur Guyader <arthur.guyader@iot.bzh>
- 	Change-Id: Iaeba75118a30c06320711fe69bf46234fd9cfee9


* Wed May 12 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 2.1.5
- Upgrade version from source commit sha: b4edb755dae608fd2df28f90ba47a6b9c3236179
- Commit message:
- 	[selinux] Allow binding access app-data
-
- 	Signed-off-by: Arthur Guyader <arthur.guyader@iot.bzh>
- 	Change-Id: Id01634e0f306cc63084232b9c7bdd405685924cf


* Tue May 11 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 2.1.4
- Upgrade version from source commit sha: 820eecbfbcf8b3dcc510bc1bfbb67c80ae64800e
- Commit message:
- 	[bug] Use label (not id) for cynagora permissions
-
- 	Signed-off-by: Arthur Guyader <arthur.guyader@iot.bzh>
- 	Change-Id: I63e06d235fd119b071654f3a61121ce41b236929


* Tue May 04 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 2.1.3
- Upgrade version from source commit sha: fcbfc3e400a18fcf7218732d04e3940730526458
- Commit message:
- 	[bug] Symbolic link point to security-manager
-
- 	Signed-off-by: Arthur Guyader <arthur.guyader@iot.bzh>
- 	Change-Id: I08ad9cfc36e716fe7bb444a3a272005f7e8912bf


* Fri Apr 30 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 2.1.2
- Upgrade version from source commit sha: 5bd276378905cf9231441ed62c5264b2d0484d1d
- Commit message:
- 	[bug] access does not have the same capability
-
- 	Signed-off-by: Arthur Guyader <arthur.guyader@iot.bzh>
- 	Change-Id: I76885311652e7a4bcde986f20ca5104ba0be2a85


* Tue Apr 27 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 2.1.1
- Upgrade version from source commit sha: 34befc7bfc8b614e21b20d7daafa4c58758be1b2
- Commit message:
- 	[bug] Fix bad path len in secure copy
-
- 	Signed-off-by: Arthur Guyader <arthur.guyader@iot.bzh>
- 	Change-Id: I68c18e88f240a74c98c828ede8a30acb7febfb58


* Tue Apr 27 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 2.1.0
- Upgrade version from source commit sha: ec7d48f52165bf3acf98a0347e5023ce69316c7d
- Commit message:
- 	[version] Update to version 2.1
-
- 	Signed-off-by: Arthur Guyader <arthur.guyader@iot.bzh>
- 	Change-Id: I51074b9264a815abeed40d3feb457171fb6e7813


* Tue Apr 20 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 2.0.9
- Upgrade version from source commit sha: 0aae789b678e099d4e3914eead2996a6790f7ff0
- Commit message:
- 	[test] Create two tests binaries (smack, selinux) and fix tests
-
- 	Signed-off-by: Arthur Guyader <arthur.guyader@iot.bzh>
- 	Change-Id: Iab06f552e7b44c90665504b7f8e08866d311228e


* Mon Apr 19 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 2.0.9
- Upgrade version from source commit sha: 7c8a61dd0d880954fd6c006f35acd8ec3f661abe
- Commit message:
- 	[test] Create two tests binaries (smack, selinux) and fix tests
-
- 	Signed-off-by: Arthur Guyader <arthur.guyader@iot.bzh>
- 	Change-Id: Iab06f552e7b44c90665504b7f8e08866d311228e


* Wed Apr 14 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 2.0.8
- Upgrade version from source commit sha: 41b875b65548ab22dc7a9b1fd92adf358812cd39
- Commit message:
- 	[security] Use secure strncpy
-
- 	Signed-off-by: Arthur Guyader <arthur.guyader@iot.bzh>
- 	Change-Id: I3c2e5a8cb2cd88449181677271776e884bf15645


* Thu Mar 25 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210325+154639+0+gba6a4eab
- Upgrade version from source commit sha: ba6a4eabcfe35fd5d80dd94c2129f1b10f672f8a
- Commit message:
- 	[version] Update to version 2.0
-
- 	Change-Id: Idb14e05bfe3df52a2faded69459b10e0e8d1c7d8


* Mon Aug 24 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 2.0.6
- Upgrade version from source commit sha: 8ba9d312aba2dcd92a6280d2da498fa784c99de4
- Commit message:
- 	[smack] Add smack rights
-
- 	r for ~APP~ on User:App-Shared
- 	x for ~APP~ on ~APP~:Http
- 	rx for ~APP~ on User:Home
-
- 	Signed-off-by: Arthur Guyader <arthur.guyader@iot.bzh>
- 	Change-Id: Id432dab2b86b75184d444999566c2addbc07f653


* Mon Aug 24 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 2.0.5
- Upgrade version from source commit sha: 041a5a34c3c77b8578efc8a659149cb5ff7809ef
- Commit message:
- 	[smack} do not generate an error if rules files already removed
-
- 	Signed-off-by: Arthur Guyader <arthur.guyader@iot.bzh>
- 	Change-Id: I4018d137e327937c26d972e72cd1cd232f38e26a


* Fri Aug 21 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 2.0.4
- Upgrade version from source commit sha: 3335c42caddb5e02cef47392953903134ac74aab
- Commit message:
- 	[smack] Do not generate an error for execute if not executable
-
- 	Signed-off-by: Arthur Guyader <arthur.guyader@iot.bzh>
- 	Change-Id: I549df6129334e0e7e69931a94e355d83d1f7d5b6


* Fri Aug 21 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 2.0.3
- Upgrade version from source commit sha: a0eb60bfaa0819b21842f6856accbda1be531a1b
- Commit message:
- 	[smack] remove is_executable for libraries
-
- 	Signed-off-by: Arthur Guyader <arthur.guyader@iot.bzh>
- 	Change-Id: I815d099766ade9c580e8c61b5299deab18e99b86


* Fri Aug 21 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 2.0.2
- Upgrade version from source commit sha: 1091565b856b65a496a8018b722671445e955032
- Commit message:
- 	[smack] Do not generate an error for transmute and execute
-
- 	label_path don't generate an error if :
-
- 	- the path is not a directory for transmute
- 	- the path is not a regular file for execute
-
- 	Signed-off-by: Arthur Guyader <arthur.guyader@iot.bzh>
- 	Change-Id: I70d0c18a58ba2082c43b20cec88a9b9417ede800


* Fri Aug 21 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 2.0.1
- Upgrade version from source commit sha: 5984230f33ca39a2c0ef191ada069c91e0cac7eb
- Commit message:
- 	Add write access on User:App-Shared
-
- 	Signed-off-by: Arthur Guyader <arthur.guyader@iot.bzh>
- 	Change-Id: I597f94a061d581f2b73a228c3b33f77262e8c264


* Thu Aug 20 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 2.0.0
- Upgrade version from source commit sha: 37b3fb16e1143ac82d0181abc0550044be8da74f
- Commit message:
- 	[BUG] remove fc file install in CMakeLists
-
- 	Signed-off-by: Arthur Guyader <arthur.guyader@iot.bzh>
- 	Change-Id: Ied5fb00f64acc558b3e83139b68f7253113f4a8d



* Thu Aug 20 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> ge61f91bb
- Upgrade version from source commit sha: e61f91bbb408897b28a8b286c07b4aa240f5393d
- Commit message:
- 	Security Manager
-
- 	Change-Id: I01bac76982d8a093eeb5da1ded3192a9467a2ba0
- 	Signed-off-by: Arthur Guyader <arthur.guyader@iot.bzh>

