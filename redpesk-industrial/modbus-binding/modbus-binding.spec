Name: modbus-binding
#Hexsha: 1d4332517fd2721955cdfefac02514626b463d47
Version: 2.0.1+1+g1d43325
Release: 13%{?dist}
Summary: Binding to serve an API connected to modbus hardware
Group:   Development/Libraries/C and C++
License:  Apache-2.0
URL: https://github.com/redpesk-industrial/modbus-binding
Source: %{name}-%{version}.tar.gz

%global _afmappdir %{_prefix}/redpesk

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(afb-binding)
BuildRequires:  pkgconfig(afb-helpers4-static) >= 10.0.5
BuildRequires:  pkgconfig(librp-utils-static)
BuildRequires:  pkgconfig(libmodbus) >= 3.1.6
Requires:       afb-binder

%description
%{name} Binding to serve an API connected to modbus hardware.

%package simulation
Summary: Simulate a modbus tcp device

%description simulation
Simulate a modbus tcp device

%package devel
Requires: %{name} = %{version}
Provides: pkgconfig(%{_name}) = %{version}
Summary:  %{summary} (development package)

%description devel 
%summary 
This is the development package for %{_name}.

%prep
%autosetup -p 1

%build
%cmake . -DAFM_APP_DIR=%{_afmappdir}
%cmake_build

%install
%cmake_install

%check

%clean

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%dir %{_afmappdir}/%{name}
%{_afmappdir}/%{name}/lib/modbus-binding.so
%{_afmappdir}/%{name}/.rpconfig/manifest.yml
%exclude %{_afmappdir}/%{name}/lib/plugins/*
%exclude %{_afmappdir}/%{name}/etc/*

%files devel
%dir %{_libdir}/pkgconfig
%{_includedir}/modbus-binding.h
%{_libdir}/pkgconfig/modbus.pc

%files simulation
%{_bindir}/modbus-simulation

%%changelog

* Tue Feb 27 2024 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 2.0.1+1
- Refactor without afmmacro and afb-cmake-module

* Fri Jul 23 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.1.0+20210711+6+g342f915
- Upgrade version from source commit sha: 342f915b5e6cdda9cbf17650cd70cdd04388bbc5
- Commit message:
- 	[Doc] Typo Redpesk/redpesk #2025
- 	
- 	Signed-off-by: Emilie Argouarch <emilie.argouarch@iot.bzh>


