Name:           afb-libpython
#Hexsha:        33a9623ce85bfcd4713ab8a4a7028814b27c500c
Version:        1.1.0
Release:        10%{?dist}
License:        LGPLv3
Summary:        Abstraction of afb-libafb for integration with non C/C++
Group:          Development/Libraries/C and C++
Url:            https://git.ovh.iot/redpesk/redpesk-common/afb-libpython
Source:         %{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  afb-cmake-modules
BuildRequires:  pkgconfig(libafb) >= 5.0
BuildRequires:  pkgconfig(librp-utils) >= 0.0.3
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
