#Archive: afb-libpython-2.3.0+1+gb9be36c.tar.gz
#Hexsha: b9be36cb20950d75c0e1d9515f7d3ddc936be1f5
Name:           afb-libpython
Version:        2.3.0+1+gb9be36c
Release:        19%{?dist}
License:        LGPL-3.0-only
Summary:        Abstraction of afb-libafb for integration with non C/C++
Group:          Development/Libraries/C and C++
Url:            https://git.ovh.iot/redpesk/redpesk-common/afb-libpython
Source:         %{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libafb) >= 5.0
BuildRequires:  pkgconfig(libafb-binder) >= 5.0
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-devel

%global debug_package %{nil}

%description
Exposes afb-libafb to the Python scripting language.

%prep
%setup -q -n %{name}-%{version}

%build
%cmake -DAFBCMOD_ALLOW_BUILD_IN_SOURCE=YES
%cmake_build

%install
%cmake_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{python3_sitearch}/*.so
