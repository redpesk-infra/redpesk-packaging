#Archive: afb-monitoring-1.2.0.tar.gz
#Hexsha: 2a4ebe8b0dc372ba0741d3d09e7b434cfe999845
Name: afb-monitoring
Version: 1.2.0
Release: 6%{?dist}
Summary: Monitoring of afb-binder

License: GPL-3.0-only
URL: https://github.com/redpesk-devtools/afb-monitoring
Source: %{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: cmake
Suggests: afb-binder

%description
Monitoring file for afb-binder of version greater or equal to 5.3

%prep
%autosetup -p 1

%build
%cmake .
%cmake_build

%install
%cmake_install

%files
%defattr(-,root,root)
%dir %{_datarootdir}/afb-monitoring
%{_datarootdir}/afb-monitoring/*

%changelog

* Mon Mar 23 2026 José Bollo jose.bollo@iot.bzh 0.99.0
- creation
