#---------------------------------------------
# spec file for package afb-binder
#---------------------------------------------

Name:           afb-binder
#Hexsha: 7f723a75df35324ea030b8ed670c62b433443fcf
Version: 5.1.3+1+g7f723a7
Release: 29%{?dist}
License:        GPL-3.0-only
Summary:        Application framework binder
Url:            https://github.com/redpesk-core/afb-binder
Source:         %{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libafb) >= 5.0.1
BuildRequires:  pkgconfig(librp-utils) >= 0.0.4

%description
The application framework binder

#---------------------------------------------
%package -n libafb-binder5
Group:          Development/Libraries/C and C++
Summary:        Application Framework Binder library

%description -n libafb-binder5
Application Framework Binder library

#---------------------------------------------
%package -n libafb-binder-devel
Group:          Development/Libraries/C and C++
Requires:       libafb-binder5 = %{version}
Requires:       pkgconfig(json-c)
Requires:       pkgconfig(libafb) >= 5.0.1
Provides:       pkgconfig(libafb-binder) = %{version}
Summary:        Application Framework Binder library - Developement files

%description -n libafb-binder-devel
Application Framework Binder library - Developement files

#---------------------------------------------
%prep
%setup -q -n %{name}-%{version}

%build
%cmake .
%cmake_build

%install
%cmake_install

%post

%postun

#---------------------------------------------
%files
%defattr(-,root,root)
%{_bindir}/afb-binder
%dir %{_datarootdir}/afb-binder
%{_datarootdir}/afb-binder/*

#---------------------------------------------
%post -n libafb-binder5
/sbin/ldconfig

%postun -n libafb-binder5
/sbin/ldconfig

%files -n libafb-binder5
%defattr(-,root,root)
%{_libdir}/libafb-binder.so.*

#---------------------------------------------
%files -n libafb-binder-devel
%defattr(-,root,root)
%{_includedir}/libafb-binder.h
%{_libdir}/libafb-binder.so
%{_libdir}/pkgconfig/libafb-binder.pc

#---------------------------------------------
%changelog

* Tue Jan 10 2023 José Bollo jose.bollo@iot.bzh 5.0.0
- Version 5.0.0
- Packaging of libafb-binder

* Fri Nov 19 2021 José Bollo jose.bollo@iot.bzh 4.0.3
- [CI] Create MAINTAINERS file
- Process the "log" entry of imported config files
- [DOC] Update images URLs after new release
- Adding --rpc-client and --rpc-server options
- Prepare version 4.0.3
- Fix use of afb_sched_post_job
- Version 4.0.3

* Wed Jun 16 2021 Jose Bollo jose.bollo@iot.bzh 4.0.2
- Update test extensions to use strings
- Version 4.0.2
* Tue Apr 13 2021 José Bollo jose.bollo@iot.bzh 4.0.1

* Fri Apr 09 2021 José Bollo jose.bollo@iot.bzh 4.0.0
- doc: remove reference to @p
- Add option to get the config after expansion
- afb-binder-opts: Print the config only once
- afb-binder-book: Add scdoc's manpage
- Install pages of manual
- afb-binder: Add weak alias for downloading
- mkbuild: Allow build every where
- Document environment variables
- Version 4.0.0

* Thu Mar 25 2021 José Bollo jose.bollo@iot.bzh 4.0.0beta6
- Emit an error if the loaded config is wrong
- Update include to new headers of libafb
- Add man page
- AFB.js: Backport of angular work
- AFB.js: Fix indentation
- afb-binder: Simplify includes
- afb-binder: Initialize the global api
- Version 4.0.0beta6
