
Name: canopen-binding
#Hexsha: 0a73850cac38d7bc29103db39857d615eb8bb3a1
Version: 1.1.0
Release: 18%{?dist}
Summary: canopen-binding is a binding that allows the control of a CANopen field network

License: No license to be set
URL: http://git.ovh.iot/redpesk/redpesk-industrial/canopen-binding
Source0: %{name}-%{version}.tar.gz

BuildRequires: afm-rpm-macros
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: afb-cmake-modules
BuildRequires: pkgconfig(json-c)
BuildRequires: pkgconfig(libsystemd) >= 222
BuildRequires: pkgconfig(afb-binding)
BuildRequires: pkgconfig(afb-libcontroller)
BuildRequires: pkgconfig(libmicrohttpd) >= 0.9.55
BuildRequires: pkgconfig(afb-libhelpers)
BuildRequires: liblely-devel
BuildRequires: liblely-coapp2
BuildRequires: pkgconfig(lua) >= 5.3

%description
canopen-binding is a binding that allows the control of a CANopen field network from an Redpesk type system.
It handle different formats natively (int, float, string...) but can also handle custom formatting using plugins.
It is based on the opensource industrial c++ library Lely.

%define wgtname %{name}

Requires: afb-binder
Requires: liblely-coapp2

%prep
%autosetup -p 1

%files
%afm_files

%afm_package_test

%afm_package_devel

%build
%afm_configure_cmake
%afm_build_cmake

%install
%afm_makeinstall

%check

%clean

%changelog
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

