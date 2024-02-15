Name: dbus-binding
#Hexsha: a23a9512c45c04cf513f8fc1a2debe94537a80a8
Version: 0.0.0+20240215+113050+0+ga23a951
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