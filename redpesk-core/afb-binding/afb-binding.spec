#---------------------------------------------
# spec file for package afb-binding
#---------------------------------------------
Name:           afb-binding
#Hexsha:         cc31c8ce215674c2693c218c593c25d73ce90938
Version:        4.1.11
Release:        27%{?dist}
License:        LGPL-3.0
Summary:        Binding headers for Application Framework Binder
Group:          Development/Libraries/C and C++
Url:            https://github.com/redpesk-core/afb-binding
Source:         %{name}-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  cmake
Requires:       %{name}-devel = %{version}
%global debug_package %{nil}

%description
Development files for creating application framework bindings

#---------------------------------------------
%package devel
Summary:        Afb-binding headers
Provides:       pkgconfig(afb-binding)

%description devel
Development files for creating application framework binding

#---------------------------------------------
%package tutorial
Requires:       %{name}-devel = %{version}
Summary:        Afb-binding examples and tutorial

%description tutorial
Provides examples for creation application framework binding

#---------------------------------------------
%package doc
Requires:       %{name}-devel = %{version}
Summary:        Documentation files

%description doc
Some documentation on how to write application framework bindings

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
%file

#---------------------------------------------
%files devel
%defattr(-,root,root)
%dir %{_includedir}/afb
%{_includedir}/afb/*
%{_libdir}/pkgconfig/*.pc
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/tutorials
%dir %{_datadir}/%{name}/tutorials/v3
%dir %{_datadir}/%{name}/tutorials/v4
%{_datadir}/%{name}/tutorials/v3/*
%{_datadir}/%{name}/tutorials/v4/*

#---------------------------------------------
%files doc
%defattr(-,root,root)
%dir %{_datadir}/%{name}/docs
%{_datadir}/%{name}/docs

#---------------------------------------------
%files tutorial
%defattr(-,root,root)
%{_datadir}/%{name}/tutorials/Makefile
%{_datadir}/%{name}/tutorials/sample.txt

#---------------------------------------------
%changelog

* Thu Jan 05 2023 José Bollo jose.bollo@iot.bzh 4.1.1
- Fix reference to afb_api_new_api
- Prepare version 4.1.0
- afb-errno: Improve naming (switch ERROR to ERRNO)
- afb-errno: Create generic error for applications
- afb-binding-x4: Add userdata to requests
- Update copyrights
- Improve documentation
- hello4: Add verbs "eventstart" & "eventstop"
- Improve tutorial V4 #1
- Add metapkg file
- Version 4.1.1

* Fri Nov 19 2021 José Bollo jose.bollo@iot.bzh 4.0.3
- [CI] Create MAINTAINERS file
- tutorial: Add use of patterned verb's name
- Prepare version 4.0.3
- C++ wrapper: Fix ambiguity data constructors
- C++ wrapper: Improvement of reply, push, broadcast
- tutorial v4: Add verb getbin
- Prepare specialized interfaces for requests
- Introduce specialized HTTP interface
- afb-wrap-v[34]: Fix g++ issues
- Add tic-tac-toe tutorial
- Version 4.0.3

* Wed Jun 16 2021 Jose Bollo jose.bollo@iot.bzh 4.0.2
- Fix of tuto output
- Removes direct call interfacing
- Improve revision management of interfaces v4
- Add predefined type bytearray
- [DOC] Better signatures for the reply functions
- Add conversion for parameters of requests
- Version 4.0.2
* Tue Apr 13 2021 José Bollo jose.bollo@iot.bzh 4.0.1

* Fri Apr 09 2021 José Bollo jose.bollo@iot.bzh 4.0.0
- hello4: Add get file verb
- afb-binding-v4: Fix missing definitions
- afb-binding-v4: Fix comments
- mkbuild: Allow build every where
- Version 4.0.0

* Thu Mar 25 2021 José Bollo jose.bollo@iot.bzh 4.0.0beta6
- afb-binding-x4-itf: Modify handling of context
- More change on managing context
- Version 4.0.0beta6
