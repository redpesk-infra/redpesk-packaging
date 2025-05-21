Name: dbus-binding
#Hexsha: 6afc35ca0f0560dfd65b787852e89c57643df4dd
Version: 0.0.0+20250106+104427+0+g6afc35c
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