
Name:	       	afb-jscli
#Hexsha: 	abb5436de7a401d08986e5caf42e572db8e6cb3c
Version: 	0.3.0
Release:        2%{?dist}
Summary:        Interpreter of javascript file, based on quickjs, to interfer with bindings api
Group:          Development/Libraries/Javascript/C and C++
License:        MIT
URL:            https://github/redpesk-addons/afb-jscli
Source:		%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  pkgconfig(libsystemd) >= 222
BuildRequires:	pkgconfig(libafbcli) >= 4

%description
%summary

%prep
%setup -q -n %{name}-%{version}

%build
# erase the default options for openSUSE because it sets -Wl,--no-undefined
%cmake -DCMAKE_SHARED_LINKER_FLAGS= .
%cmake_build

%install
%cmake_install

%files
%{_bindir}/%{name}
%dir %{_datarootdir}/%{name}
%{_datarootdir}/%{name}


%changelog

* Wed Apr 20 2022 Jose Bollo jose.bollo@iot.bzh 0.3.0
- Update copyrights
- Update to newer version of libafb

* Thu Dec 02 2021 José Bollo jose.bollo@iot.bzh 0.0
- fix build issues

* Thu Dec 02 2021 José Bollo jose.bollo@iot.bzh 0.0+5+gdf40dc5
- fix build issue

* Thu Dec 02 2021 José Bollo jose.bollo@iot.bzh 0.0+4+ge265f3b
- fix build issue

* Thu Dec 02 2021 José Bollo jose.bollo@iot.bzh 0.0+3+gff5b5a8
- Fix convert

* Thu Dec 02 2021 José Bollo jose.bollo@iot.bzh 0.0+2+gd1f6456
- Fix link option of modules

* Thu Dec 02 2021 José Bollo jose.bollo@iot.bzh 0.0+1+gee2d3c0
- Fix link option of modules
