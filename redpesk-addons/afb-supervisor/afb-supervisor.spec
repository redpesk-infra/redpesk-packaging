#---------------------------------------------
# spec file for package afb-supervisor
#---------------------------------------------

Name:           afb-supervisor
#Hexsha: a5ebcd320b312012e48d93b990b069e48c05b086
Version: 4.2.1
Release: 7%{?dist}
License:        GPL-3.0-only
Summary:        Supervisor of application framework binder
Url:            https://git.ovh.iot/redpesk/redpesk-addons/afb-supervisor
Source:         %{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libsystemd) >= 222
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libafb) >= 5.0

%description
Provides the supervisor daemon and service for afb-binder

#---------------------------------------------
%prep
%setup -q -n %{name}-%{version}

%build
%cmake -DUNITDIR_SYSTEM=%{_unitdir} .
%cmake_build

%install
%cmake_install

%post

%postun

#---------------------------------------------
%files
%defattr(-,root,root)
%dir %{_bindir}
%{_bindir}/afb-supervisor
%dir %{_unitdir}
%{_unitdir}/afb-supervisor.service
%{_unitdir}/afm-api-supervisor.service
%{_unitdir}/afm-api-supervisor.socket

#---------------------------------------------
%changelog

* Fri Jan 20 2023 José Bollo jose.bollo@iot.bzh 4.2.0
Bump to version 4.2.0

* Wed Apr 20 2022 Jose Bollo jose.bollo@iot.bzh 4.1.0
- Update copyrights
- Update to newer version of libafb
* Fri Jul 23 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 4.0.1+20210711+1+g39290e6
- Upgrade version from source commit sha: 39290e67c552eb535ba821fde55a657001e1d5b2
- Commit message:
- 	[CI] Create MAINTAINERS file
-
- 	Change-Id: I3109b143fad4bed6cba8d255ed2fd9b6e800a6e0



* Thu Jul 01 2021 José Bollo jose.bollo@iot.bzh 4.0.1
- mkbuild: Allow build every where
- Version 4.0.1
