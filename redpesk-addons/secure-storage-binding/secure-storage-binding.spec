#Archive: secure-storage-binding-1.0.1.tar.gz
#Hexsha: baaf983c12f6218c218fb567211bf2132a1dbe4c
Name: secure-storage-binding
Version: 1.0.1
Release: 0%{?dist}
Summary: Binding provide a database API with key/value semantics
Group:   Development/Libraries/C and C++
License:  Apache-2.0
URL: https://github.com/redpesk-addons/secure-storage-binding
Source: %{name}-%{version}.tar.gz

BuildRequires:  afm-rpm-macros
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  afb-cmake-modules
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(lua) >= 5.3
BuildRequires:  pkgconfig(afb-binding)
BuildRequires:  pkgconfig(afb-helpers4)
BuildRequires:  pkgconfig(afb-libcontroller)
BuildRequires:  pkgconfig(libsystemd) >= 222


%if 0%{?suse_version}
BuildRequires:  libdb-4_8-devel
%else
BuildRequires:  libdb-devel
%endif

Requires:       afb-binder

%description
This binding provide a database API with key/value semantics.
The backend is currently a Berkeley DB.

%package redtest
Summary: redtest package (coverage build)
Requires: %{name}
Requires: lcov
Requires: afb-test-py
Requires: afb-libpython

%description redtest
This package contains binaries built with coverage instrumentation.v

%prep
%autosetup -p 1

%build
%afm_configure_cmake
%afm_build_cmake

%install
export NO_BRP_STRIP_DEBUG="true"
%afm_makeinstall

mkdir -p %{buildroot}%{_libexecdir}/redtest/%{name}/
cp ./redtest/run-redtest %{buildroot}%{_libexecdir}/redtest/%{name}/
cp ./test/*.py          %{buildroot}%{_libexecdir}/redtest/%{name}/

%check

%clean

%files
%afm_files

%files redtest
%defattr(-,root,root)

%{_libexecdir}/redtest/%{name}/*.py
%{_libexecdir}/redtest/%{name}/run-redtest



%%changelog
