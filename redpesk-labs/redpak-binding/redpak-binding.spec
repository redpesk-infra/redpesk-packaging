#Archive: redpak-binding-1.0.0+14+g4fc5df4.tar.gz
#Hexsha: c8b42d602d178e28764106bd4fedd53b618b97ef

Name:           redpak-binding
Version:        1.1.0
Release: 5%{?dist}
Summary:        This service aims to manage Rednode on target.
Group:          Development/Libraries/C and C++
License:        APL2.0
URL:            https://github.com/redpesk-labs/redpak-binding
Source:         %{name}-%{version}.tar.gz

%global _afmappdir %{_prefix}/redpesk

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(afb-binding) >= 4
BuildRequires:  pkgconfig(red-pak) >= 2.3
BuildRequires:  pkgconfig(librp-utils-json-c-static)
BuildRequires:  afb-idl

Requires: afb-binder

%description
%summary

%prep
%autosetup -p 1

%build
%cmake -DAFM_APP_DIR=%{_afmappdir} .
%cmake_build

%install
%cmake_install

%files
%defattr(-,root,root,-)
%dir %{_afmappdir}/%{name}
%{_afmappdir}/%{name}/lib/
%{_afmappdir}/%{name}/.rpconfig/

%changelog

* Wed Jul 08 2026 José Bollo jose.bollo@iot.bzh 1.1
- repakage
