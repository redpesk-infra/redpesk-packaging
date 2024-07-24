
Name: canopen-binding
#Hexsha: 1f5a80bd23c9303f9d352ec7fdfb33b7f6192cee
Version: 2.1.0
Release: 31%{?dist}
Summary: canopen-binding is a binding that allows the control of a CANopen field network

License: No license to be set
URL: http://git.ovh.iot/redpesk/redpesk-industrial/canopen-binding
Source: %{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(json-c)
BuildRequires: pkgconfig(afb-binding)
BuildRequires: pkgconfig(librp-utils-static)
BuildRequires: pkgconfig(afb-helpers4-static)
BuildRequires: liblely-devel
BuildRequires: liblely-coapp2

Requires: afb-binder
Requires: liblely-coapp2

%global _afmappdir %{_prefix}/redpesk

%description
canopen-binding is a binding that allows the control of a CANopen field network from an Redpesk type system.
It handle different formats natively (int, float, string...) but can also handle custom formatting using plugins.
It is based on the opensource industrial c++ library Lely.

%package devel
Requires: %{name} = %{version}
Provides: pkgconfig(%{name}) = %{version}
Summary:  %{summary} (development package)

%description devel 
%summary 
This is the development package for plugins of %{name}.

%prep
%autosetup -p 1

%build
%cmake . -DAFM_APP_DIR=%{_afmappdir}
%cmake_build

%install
%cmake_install

%files
%dir %{_afmappdir}
%{_afmappdir}/%{name}
%{_libdir}/libCANopenEncoder.so

%files devel
%dir %{_libdir}/pkgconfig
%{_libdir}/libCANopenXchg.a
%{_libdir}/pkgconfig/CANopen.pc
%{_libdir}/pkgconfig/CANopenXchg.pc
%{_includedir}/CANopen
%{_bindir}/dcf2afb.py

%check

%clean

%changelog

* Wed Jul 24 2024 José Bollo jose.bollo@iot.bzh 2.1.0
- Add CANopenXchg items

* Fri Jul 23 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.1.0+20210711+8+g0a73850
- Upgrade version from source commit sha: 0a73850cac38d7bc29103db39857d615eb8bb3a1
- Commit message:
- 	[Doc] Typo Redpesk/redpesk #2025
- 	
- 	Signed-off-by: Emilie Argouarch <emilie.argouarch@iot.bzh>


* Fri Jul 23 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.1.0+20210711+8+g0a73850
- Upgrade version from source commit sha: 0a73850cac38d7bc29103db39857d615eb8bb3a1
- Commit message:
- 	[Doc] Typo Redpesk/redpesk #2025
- 	
- 	Signed-off-by: Emilie Argouarch <emilie.argouarch@iot.bzh>


* Fri Jul 23 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.1.0+20210711+5+gdad69f8
- Upgrade version from source commit sha: dad69f8a0df895eda4d754c11e6730ec5bed070e
- Commit message:
- 	[CI] Create MAINTAINERS file
- 	
- 	Change-Id: I374e945f4f87e02b8079e49d4f5f7eecf14c6bd2


* Thu Dec 10 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20201210+103435+0+g46557932
- Upgrade version from source commit sha: 465579320e0c260475c730052052162c5b1613e6
- Commit message:
- 	pakaging : Wip

