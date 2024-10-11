#---------------------------------------------
# spec file for package afb-client
#---------------------------------------------

Name:           afb-client
#Hexsha:        59d9a196426c7144ac2725bd615d1eb972f1ed33
Version:        4.2.1
Release:        15%{?dist}
License:        GPL-3.0-only
Summary:        Application framework binder
Group:          Development/Libraries/C and C++
Url:            https://git.ovh.iot/redpesk/redpesk-core/afb-client
Source:         %{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  pkgconfig(libsystemd) >= 222
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libafbcli) >= 4.0
BuildRequires:  gcc-c++

BuildRequires:  readline-devel

%description
Provides a basic client for the agl binder

#---------------------------------------------
%prep
%setup -q -n %{name}-%{version}

%build
%cmake .
%cmake_build

%install
%cmake_install

%post

%postun

#---------------------------------------------
%files
%defattr(-,root,root)
%{_bindir}/afb-client

#---------------------------------------------
%changelog
* Tue Apr 13 2021 José Bollo jose.bollo@iot.bzh 4.0.1

* Fri Apr 09 2021 José Bollo jose.bollo@iot.bzh 4.0.0
- Adapt to cmake 3.10
- Version 4.0.0beta6
- mkbuild: Allow build every where
- Version 4.0.0
