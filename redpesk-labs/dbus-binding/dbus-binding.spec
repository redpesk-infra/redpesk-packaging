%define debug_package %{nil}
ExcludeArch: x86_64

Name: dbus-binding
#Hexsha: 5e74d5f8ea2ea5a12e1a3dffa42e331a0da6b1b1
Version: 0.0.0+20240213+131343+0+g5e74d5f
Release: 1%{?dist}
Summary: Binding to serve an API connected to dbus
Group:   Development/Libraries/C and C++
License:  GPLv3
URL: https://github.com/redpesk-labs/dbus-binding
Source: %{name}-%{version}.tar.gz

BuildRequires:  afm-rpm-macros
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  afb-cmake-modules
BuildRequires:  pkgconfig(afb-binding)
BuildRequires:  pkgconfig(afb-libhelpers)
BuildRequires:  pkgconfig(libsystemd) >= 222
BuildRequires:  pkgconfig(librp-utils-static)
BuildRequires:  pkgconfig(afb-helpers4-static)

Requires:       afb-binder
ExcludeArch: x86_64

%description
%{name} Binding to serve an API connected to dbus.

%prep
%autosetup -p 1

%files
%afm_files
%exclude %{_afmdatadir}/%{name}/lib/plugins/*.ctlso
%exclude %{_afmdatadir}/%{name}/etc/*.json

%build
%afm_configure_cmake
%afm_build_cmake

%install
%afm_makeinstall

mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/.rpconfig
cp ./rpconfig/manifest.yml %{buildroot}%{_prefix}/redpesk/%{name}/.rpconfig/manifest.yml

%check

%clean

%%changelog