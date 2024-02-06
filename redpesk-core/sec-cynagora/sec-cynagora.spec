%define debug_package %{nil}

Name:           sec-cynagora
#Hexsha:        bdfeeb6d48d97fc9bcd4ec634e59665069d03e19
Version:        2.2.3
Release: 18%{?dist}
Summary:        Cynara service with client libraries

License:        Apache-2.0
URL:            https://github.com/redpesk-core/sec-cynagora
Source:         %{name}-%{version}.tar.gz
Source2:        cynagora-redpesk.initial

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libsystemd) >= 222
BuildRequires:  libcap-devel

Requires(pre):  /usr/bin/getent
Requires(pre):  /usr/sbin/useradd
Requires(pre):  /usr/sbin/groupadd


%description
%{summary}.

%package devel
Summary:        Development libraries and header files for cynagora
Requires:       %{name} = %{version}
Provides:       pkgconfig(cynagora) = %{version}

%description devel
%{summary}.

%prep
%autosetup -p 1

%build
%cmake -DSYSTEMD_UNIT_DIR=/usr/lib/systemd/system  -DWITH_SYSTEMD=ON  -DWITH_CYNARA_COMPAT=OFF
%cmake_build

%install
%cmake_install
cp %{SOURCE2} %{buildroot}/%{_sysconfdir}/security/cynagora.initial

%pre
getent group cynagora >/dev/null || groupadd -r cynagora ||:
getent passwd cynagora >/dev/null || useradd --system --home %{_localstatedir}/lib/empty --no-create-home --shell /bin/false --gid cynagora cynagora || :
ldconfig

%post
ldconfig

%files
%defattr(-,root,root)
%config %{_sysconfdir}/security/cynagora.initial
%{_unitdir}
%{_unitdir}/sockets.target.wants
%{_libdir}/libcynagora*.so.*
%{_bindir}/*
%defattr(-,cynagora,cynagora)
%{_localstatedir}/lib/cynagora

%files devel
%{_includedir}/cynagora.h
%{_libdir}/pkgconfig/cynagora.pc
%{_libdir}/libcynagora*.so

%changelog

* Wed Jun 16 2021 Jose Bollo jose.bollo@iot.bzh 2.2.1
- Fix mixing synchronous and asynchronous communication
- Version 2.2.1

* Wed Jun 09 2021 José Bollo jose.bollo@iot.bzh 2.2.0
- Version 2.2.0
* Tue May 18 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 2.1.4
- Upgrade version from source commit sha: 49c34f906778837ebd7ecc8cac7e98615a57c5d8
- Commit message:
- 	Add 'clearall' for clearing all cachings
-
- 	Change-Id: If36316365fa9d015b29c9e5d93e23ea112240db6

* Thu Apr 08 2021 José Bollo jose.bollo@iot.bzh 2.1.3
- [CMake] Add libcap dependency.
- Create default database directory
- Version 2.1.3

* Tue Apr 06 2021 José Bollo jose.bollo@iot.bzh 2.1.2
- set queries to NULL in cynagora_create
- cynagora.h: Fix comment
- main-cynagora-admin: Emit a diagnostic status
- Improve error report
- filedb: Add check of rules when opening
- Add macro for testing index type
- Version 2.1.2

* Fri Nov 27 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 2.1
- Upgrade version from source commit sha: 7d7907651c42c5c32deabc17b639e0e1765eae60
- Commit message:
- 	Version 2.1
- 	
- 	The version 2.1 fixes a database issue.
- 	
- 	Bug-AGL: SPEC-3677
- 	
- 	Change-Id: I5c8e4595894ee26a2018f939a42ba0b8abcad722
- 	Signed-off-by: José Bollo <jose.bollo@iot.bzh>

* Mon Nov 23 2020 Jobol <jobol@iot.bzh> 2.1
- version 2.1
- Fix database issue

* Wed Apr 01 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 8.99.5+3+g218dad2e
- Upgrade version from source commit sha: 218dad2eddcbedaede44753e64ea7c30b73b00aa
- Commit message:
- 	Change cynagora service
-
- 	Remove After unit to avoid infinit waiting
- 	of afm-system-setup.service before killing it
-
- 	Bug-AGL: SPEC-3002
-
- 	Signed-off-by: Frederic Marec <frederic.marec@iot.bzh>
- 	Change-Id: I3d2348d495067186f676066ff33f77f8f0adb269


* Wed Apr 01 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 2.1
- Upgrade version from source commit sha: 218dad2eddcbedaede44753e64ea7c30b73b00aa
- Commit message:
- 	Change cynagora service
-
- 	Remove After unit to avoid infinit waiting
- 	of afm-system-setup.service before killing it
-
- 	Bug-AGL: SPEC-3002
-
- 	Signed-off-by: Frederic Marec <frederic.marec@iot.bzh>
- 	Change-Id: I3d2348d495067186f676066ff33f77f8f0adb269

* Wed Nov 06 2019 Clément Bénier <clement.benier@iot.bzh>
- grouadd, useradd cynagora

* Tue Nov 05 2019 Clément Bénier <clement.benier@iot.bzh>
- initial creation
