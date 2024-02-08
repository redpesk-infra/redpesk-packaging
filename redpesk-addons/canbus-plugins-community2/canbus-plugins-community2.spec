
Name: canbus-plugins-community2
%global _name canbus-plugins-community
%global _afmappdir %{_prefix}/redpesk

#Hexsha: 4ca7f2409d6cfc03e3f5cef9c83f938264621da2
Version: 2.0.2
Release: 12%{?dist}
Summary: Plugins for canbus-binding
Group:          Development/Libraries/C and C++
License: APL2.0
URL: https://github.com/redpesk-common/canbus-plugins-community
Source: %{name}-%{version}.tar.gz

Conflicts: %{_name}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kernel-headers
BuildRequires:  pkgconfig(canbus-binding) >= 2
BuildRequires:  canbus-generator >= 2

Requires: canbus-binding >= 2

%description
%summary

%package -n canbus-plugins2-obd2
Summary: obd2 signals plugin
%description -n canbus-plugins2-obd2
%summary

%package -n canbus-plugins2-engine
Summary: engine signals plugin
%description -n canbus-plugins2-engine
%summary


%package -n canbus-plugins2-hvac
Summary: hvac signal plugin
%description -n canbus-plugins2-hvac
%summary

%package -n canbus-plugins2-vcar
Summary: vcar signals plugin
%description -n canbus-plugins2-vcar
%summary

%prep
%autosetup -p 1 -n %{name}-%{version}

%build

%cmake . -DAFM_APP_DIR=%{_afmappdir}
%cmake_build

%install
%cmake_install

%check

%clean

%files -n canbus-plugins2-obd2
%dir %{_afmappdir}/obd2-signals
%{_afmappdir}/obd2-signals

%files -n canbus-plugins2-engine
%dir %{_afmappdir}/engine-signals
%{_afmappdir}/engine-signals

%files -n canbus-plugins2-hvac
%dir %{_afmappdir}/hvac-signals
%{_afmappdir}/hvac-signals

%files -n canbus-plugins2-vcar
%dir %{_afmappdir}/vcar-signals
%{_afmappdir}/vcar-signals

%changelog

* Thu Sep 07 2023 IoT.bzh <redpesk.list.iot.bzh> 2.0.0
- Creation of the spec file
