Name: dbus-binding
#Hexsha: 0dadd55926a41dcc5dec12b7d7d497eab313442a
Version: 0.0.0+20240215+164934+0+g0dadd55
Release: 1%{?dist}
Summary: Binding to serve an API connected to dbus
Group:   Development/Libraries/C and C++
License:  GPLv3
URL: https://github.com/redpesk-labs/dbus-binding
Source: %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(afb-binding)
BuildRequires:  pkgconfig(libsystemd) >= 222
BuildRequires:  pkgconfig(json-c)

Requires:       afb-binder

%description
%{name} Binding to serve an API connected to dbus.

%prep
%autosetup -p 1

%build
%cmake . 
%cmake_build

%install
%cmake_install

%files
%dir %{_prefix}/redpesk/%{name}
%{_prefix}/redpesk/%{name}/.rpconfig/*
%{_prefix}/redpesk/%{name}/lib/*

%check

%clean

%%changelog