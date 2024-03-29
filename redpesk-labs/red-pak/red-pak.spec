Name:           red-pak
#Hexsha:        4b8b7ae65729bd8782075d7e0479db0e0a64fc3a
Version: 2.2.0+1+g4b8b7ae
Release: 14%{?dist}
Summary:        red-pak
License:        ISC
URL:			https://github.com/redpesk-labs/red-pak
Source:         %{name}-%{version}.tar.gz
BuildRequires:	redrpm-devel
BuildRequires:  libyaml-devel
BuildRequires:	libcyaml-devel
BuildRequires:	libdnf5-devel
BuildRequires:	libdnf5-cli-devel
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(uuid)
BuildRequires:  libassuan-devel
BuildRequires:  userspace-rcu-devel
BuildRequires:  check-devel

Requires: redpak-core = %{version}
Requires: red-microdnf

%description
%{summary}.

%package -n redpak-core
Summary:        libraires and binaries for red-pak
Requires:		libdnf5
Requires:		redrpm
Requires:		libcyaml
Requires:       userspace-rcu

%description -n redpak-core
%{summary}.

%package devel
Summary:        Development libraries and header files for %{name}
Requires:       redpak-core = %{version}
Provides:       pkgconfig(%{name}) = %{version}
Requires:		libcyaml-devel
Requires:		libdnf5-devel
Requires:		libdnf5-cli-devel
Requires:       userspace-rcu-devel

%description devel
%{summary}.

%package -n python3-redconf
Summary:  redconf python binding
Requires:       %{name} = %{version}

%description -n python3-redconf
%{summary}.

%prep
%autosetup -p 1

%build
%ifnarch x86_64
CFLAGS="$CFLAGS -DCONFIG_RCU_HAVE_CLOCK_GETTIME"
%endif

%cmake -DPYTHON_EXECUTABLE=%{__python3} -DPython3_EXECUTABLE=%{__python3}
%cmake_build

%install
%cmake_install

%files

%files -n redpak-core
%defattr(-,root,root)
%{_sysconfdir}/bash_completion.d/red*
%{_sysconfdir}/redpak/templates.d/*
%{_bindir}/redwrap
%{_bindir}/redwrap-dnf
%{_bindir}/redconf
%{_libdir}/libred*.so*
%{_libdir}/rpm-plugins/redpak.so


%files -n python3-redconf
%{python3_sitearch}/*.so

%files devel
%defattr(-,root,root)
%{_includedir}/*.h
%{_includedir}/*.hpp
%{_libdir}/pkgconfig/*.pc

%changelog
* Tue Dec 21 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.0.0
- Upgrade version from source commit sha: bd11881f50ae627a0641448ae0b307a9a9e2877e
- Commit message:
- 	cgroups: add feature cgroups
- 	
- 	Signed-off-by: Clement Benier <clement.benier@iot.bzh>


* Tue Nov 30 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20211130+103028+0+g4280263
- Upgrade version from source commit sha: 42802638a321a2b8c2a31a2eb3c5d53ad7b6db60
- Commit message:
- 	redlib: use global_options
- 	
- 	Signed-off-by: Clement Benier <clement.benier@iot.bzh>


* Mon Sep 13 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210913+110156+0+g6519839
- Upgrade version from source commit sha: 6519839d426f43d9f49b79159f93e46b90067493
- Commit message:
- 	redwrap-node: remove scan export logs
- 	
- 	Signed-off-by: Clement Benier <clement.benier@iot.bzh>


* Fri Sep 10 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210910+174849+0+g4b72083
- Upgrade version from source commit sha: 4b72083ce2eed2fc178cef80aafd9c7d9780c607
- Commit message:
- 	templates: admin add redpak-admin
- 	
- 	Signed-off-by: Clement Benier <clement.benier@iot.bzh>


* Tue Sep 07 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210907+174931+0+g3919cd3
- Upgrade version from source commit sha: 3919cd3207efdfa5105a8a8896b2a11d9af0f6d3
- Commit message:
- 	debug: remove
- 	
- 	Signed-off-by: Clement Benier <clement.benier@iot.bzh>


* Tue Sep 07 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210907+173922+0+gb168be0
- Upgrade version from source commit sha: b168be0117b3181880c489d9ff4f2b6e27b4ba76
- Commit message:
- 	printf: remove
- 	
- 	Signed-off-by: Clement Benier <clement.benier@iot.bzh>


* Tue Sep 07 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210907+165423+0+g74ad433
- Upgrade version from source commit sha: 74ad433f326f01c2117dfa46a171aeb7112fe2e3
- Commit message:
- 	reconfig: fix cachedir
- 	
- 	Signed-off-by: Clement Benier <clement.benier@iot.bzh>


* Tue Sep 07 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210907+162621+0+g2e52c4e
- Upgrade version from source commit sha: 2e52c4e3b3420dbf8a4e0f7fab971dd63809bc5a
- Commit message:
- 	redconf-utils: overload cachedir
- 	
- 	Signed-off-by: Clement Benier <clement.benier@iot.bzh>


* Tue Sep 07 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210907+153910+0+g480f464
- Upgrade version from source commit sha: 480f464ab527bd58b59ff22b78b870ee1e34ea7e
- Commit message:
- 	fix: system-admin.yaml
- 	
- 	Signed-off-by: Clement Benier <clement.benier@iot.bzh>


* Tue Sep 07 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210907+145459+0+g04455e6
- Upgrade version from source commit sha: 04455e6e1a75d0443169873d38a3d7d761b65f6e
- Commit message:
- 	fix: main-system.yaml template
- 	
- 	Signed-off-by: Clement Benier <clement.benier@iot.bzh>


* Tue Sep 07 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210907+143326+0+g960e98f
- Upgrade version from source commit sha: 960e98f0e9115cef5c0e2a2267629fe8513d9741
- Commit message:
- 	fix leaf node scan twice
- 	
- 	Signed-off-by: Clement Benier <clement.benier@iot.bzh>


* Fri Sep 03 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210903+161130+0+g26efb71
- Upgrade version from source commit sha: 26efb71a51399bb463051cb3cafe15ab2681f059
- Commit message:
- 	templates.d: new templates
-
- 	Signed-off-by: Clement Benier <clement.benier@iot.bzh>


* Thu Aug 26 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210826+111905+0+g4c193e8
- Upgrade version from source commit sha: 4c193e87f4b06d8c937dfcb6ba867ea3a646f8d3
- Commit message:
- 	redconfig: fix symlink creation
-
- 	Signed-off-by: Clement Benier <clement.benier@iot.bzh>


* Thu Aug 26 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210826+104733+0+g749e90d
- Upgrade version from source commit sha: 749e90d173afa7c8c654896444cdad10ecad229b
- Commit message:
- 	redwrap-dnf: fix redmicrodnf exec
-
- 	Signed-off-by: Clement Benier <clement.benier@iot.bzh>


* Wed Aug 25 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210825+163744+0+g1e027cf
- Upgrade version from source commit sha: 1e027cf35ebecfe3ef0edacab7c8e7ff5dfcface
- Commit message:
- 	redconfig: create symlink for node system to /var/lib/rpm
-
- 	Signed-off-by: Clement Benier <clement.benier@iot.bzh>


* Wed Aug 25 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210825+162935+0+gf514101
- Upgrade version from source commit sha: f514101aea84994f863ec05302a43a550d8ad48b
- Commit message:
- 	redwrap-dnf: REDMICRODNF_CMD
-
- 	Signed-off-by: Clement Benier <clement.benier@iot.bzh>


* Wed Aug 25 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210825+160615+0+gd22c2c6
- Upgrade version from source commit sha: d22c2c6b30fef6a57488e26c21881416e8c956ef
- Commit message:
- 	redwrap-conf: fprintf use format
-
- 	Signed-off-by: Clement Benier <clement.benier@iot.bzh>


* Wed Aug 25 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210825+153013+0+gd8588fc
- Upgrade version from source commit sha: d8588fcd002cfccfef1d45ae7e63d0e7ca93e6d8
- Commit message:
- 	warnings: fixed
-
- 	Signed-off-by: Clement Benier <clement.benier@iot.bzh>


* Wed Aug 25 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210825+152023+0+g8ab6876
- Upgrade version from source commit sha: 8ab68764f885bf7346b24a192fc0864eff4c90c9
- Commit message:
- 	redwrap: out node or not
-
- 	Signed-off-by: Clement Benier <clement.benier@iot.bzh>


* Wed Aug 25 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210825+111607+0+g50c1230
- Upgrade version from source commit sha: 50c1230cfcf25edc7fffd9b4dfca8313aecf96c8
- Commit message:
- 	redwrap-dnf: fix loop
-
- 	Signed-off-by: Clement Benier <clement.benier@iot.bzh>


* Tue Aug 24 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210824+151626+0+g70e94e4
- Upgrade version from source commit sha: 70e94e4c74f130e55a009f9f4af7fba2745c73db
- Commit message:
- 	redwrap-dnf
-
- 	Signed-off-by: Clement Benier <clement.benier@iot.bzh>


* Tue Aug 24 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210824+145500+0+gba7fc58
- Upgrade version from source commit sha: ba7fc580391e7f2f6e4faafe23ab8a7ad5cb3e33
- Commit message:
- 	redwrap-dnf commands
-
- 	Signed-off-by: Clement Benier <clement.benier@iot.bzh>


* Mon Aug 16 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210816+152501+0+gf1dee77
- Upgrade version from source commit sha: f1dee77dfced18284e38e50c42a5a13ef8599aca
- Commit message:
- 	red-plugin: install rpm plugin
-
- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


* Fri Jul 30 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210730+102344+0+g69fdb60
- Upgrade version from source commit sha: 69fdb60e56bd6c432e39387c6658872279146783
- Commit message:
- 	rpm-plugins: fix includedirs
-
- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


* Thu Jul 29 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210729+174647+0+g445dbe0
- Upgrade version from source commit sha: 445dbe00cc8cb952a6524fd752c7e85420321b19
- Commit message:
- 	red-plugin: rpm plugin for red-pak
-
- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


* Thu Jul 29 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210729+151639+0+g7ac2dce
- Upgrade version from source commit sha: 7ac2dce9fb2134e8e246a5b12d8af7a293c0a8c0
- Commit message:
- 	CMakeLists: RPM_LIBRAIRIES
-
- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


* Thu Jul 29 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210729+150640+0+ge383d58
- Upgrade version from source commit sha: e383d58836578e7356457097c54a7e97d1590c87
- Commit message:
- 	CMakeLists: adapt link libraires and headers
-
- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


* Thu Jul 29 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210729+150338+0+gaa94901
- Upgrade version from source commit sha: aa94901e481d1686349207992cd117a38a0f444b
- Commit message:
- 	CMakeLists: adapt link libraires and headers
-
- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


* Thu Jul 29 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210729+145746+0+gfcdaae8
- Upgrade version from source commit sha: fcdaae8619d26e2eafb9ee95ed339bcda8414de4
- Commit message:
- 	CMakeLists: adapt link libraires and headers
-
- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


* Thu Jul 29 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210729+145409+0+g38927b5
- Upgrade version from source commit sha: 38927b5c4a37cb1377b0bd083deb42f4d90e6428
- Commit message:
- 	CMakeLists: adapt link libraires and headers
-
- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


* Thu Jul 29 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210729+120320+0+gf0d49ae
- Upgrade version from source commit sha: f0d49aed308e1c3bf46058d8ef56390726b61525
- Commit message:
- 	CMakeLists: adapt link libraires and headers
-
- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


* Tue Jul 27 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210727+144446+0+g2f103ce
- Upgrade version from source commit sha: 2f103cef613ebc0f0c9fab7dfcc7d1674eb84748
- Commit message:
- 	red-conf: fix public_header
-
- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


* Tue Jul 27 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210727+143756+0+g8ca2a8d
- Upgrade version from source commit sha: 8ca2a8d723274bd4419f40764e1d02df18377936
- Commit message:
- 	red-conf: fix public_header
-
- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


* Tue Jul 27 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210727+143200+0+g0317fea
- Upgrade version from source commit sha: 0317fea7c5ec373efc0547696edf5db05613824d
- Commit message:
- 	red-conf: fix public_header
-
- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


* Tue Jul 27 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210727+140558+0+g55abca5
- Upgrade version from source commit sha: 55abca5dc835c29ad262e85e8acc4e6bd94ece0d
- Commit message:
- 	red-conf: fix public_header
-
- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


* Tue Jul 27 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210727+124623+0+g0bca590
- Upgrade version from source commit sha: 0bca590073433131682f3c37592047098f8d887d
- Commit message:
- 	red-conf: add header
-
- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


* Tue Jul 27 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210727+122824+0+g5639ed6
- Upgrade version from source commit sha: 5639ed680a4b1a59d06328d871244e7ee2c7bfa9
- Commit message:
- 	red-lib: install header
-
- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


* Tue Jul 27 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210727+111410+0+gfe1f903
- Upgrade version from source commit sha: fe1f90379c5c8435928b2c48350dc9b8463c3ab6
- Commit message:
- 	.pc: add VERSION
-
- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


* Mon Jul 26 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210726+164511+0+gbe0bb41
- Upgrade version from source commit sha: be0bb41c16c4121ced087cbc4b841cd813fe54a4
- Commit message:
- 	install .pc file
-
- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


* Mon Jul 26 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210726+162509+0+gd8820a3
- Upgrade version from source commit sha: d8820a37f5b8b9a2af56635c4b7eaa224f7c52d7
- Commit message:
- 	install .pc file
-
- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


* Mon Jul 26 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210726+160042+0+ga798b82
- Upgrade version from source commit sha: a798b82616cfd812c28dc57a596507752611100e
- Commit message:
- 	fix red-wrap bindir
-
- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


* Mon Jul 26 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210726+153641+0+g0d8fa07
- Upgrade version from source commit sha: 0d8fa07907039ba3a008d8328cc0c5680268934c
- Commit message:
- 	include(GNUInstallDirs)
-
- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


* Mon Jul 26 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210726+151339+0+g69ae29d
- Upgrade version from source commit sha: 69ae29d510f4873440d4613d499b41165750db32
- Commit message:
- 	fix CMakeLists.txt
-
- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


* Mon Jul 26 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210726+150650+0+gb621da6
- Upgrade version from source commit sha: b621da69a9fc85feff24e2cbf454b6160577c5b9
- Commit message:
- 	fix CMakeLists.txt
-
- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


* Mon Jul 26 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210726+145123+0+g98a31d2
- Upgrade version from source commit sha: 98a31d29cfb8fe91c8555388dc108199634fa9be
- Commit message:
- 	remove former directories
-
- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


* Mon Jul 26 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210726+113358+0+g900455e
- Upgrade version from source commit sha: 900455e75db192780e2aa7bc1714f81467f56a38
- Commit message:
- 	remove microdnf: use patch repository instead
-
- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


* Fri Jul 23 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210723+153018+0+gb7651c0
- Upgrade version from source commit sha: b7651c0d97105501426e81d50c643f697d9f82aa
- Commit message:
- 	CMakeLists: add libdnf5-cli
-
- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


* Thu Jul 22 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210722+111149+0+g2240f46
- Upgrade version from source commit sha: 2240f46d7ffe22e7d73886d330fe70fd3cc7de3f
- Commit message:
- 	draft6
-
- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


