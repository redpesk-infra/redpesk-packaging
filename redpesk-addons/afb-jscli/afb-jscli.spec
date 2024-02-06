
Name:	       	afb-jscli
#Hexsha: 	8d11e69a2400be7f45b29110d5a87bbceefe481d
Version: 	0.3.0
Release:        2%{?dist}
Summary:        Interpreter of javascript file, based on quickjs, to interfer with bindings api
Group:          Development/Libraries/Javascript/C and C++
License:        APL-2.0
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
%if 0%{?fedora} >= 33
%cmake_build
%else
%__make %{?_smp_mflags}
%endif

%install
[ -d build ] && cd build
%if 0%{?fedora} >= 33
%cmake_install
%else
%make_install
%endif

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
