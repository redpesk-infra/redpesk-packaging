Name: rp-lib-utils
#Hexsha: 809a33cbd2d90a612e1b2cab46f28aac92c64a7b
Version: 0.0.9
Release: 17%{?dist}
Summary: Library of utilities

License: MIT
URL: https://github.com/redpesk-core/rp-lib-utils
Source: %{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: cmake
BuildRequires: pkgconfig(json-c)
BuildRequires: pkgconfig(yaml-0.1)
BuildRequires: pkgconfig(libsystemd) >= 222
BuildRequires: libcurl-devel

%description
Library of redpesk C utilities

%package -n librp-utils0
Summary: Library of redpesk C utilities

%description  -n librp-utils0
Development files for static library of utilities

%package -n librp-utils-headers
Summary: Headers of library of utilities

%description -n librp-utils-headers
Headers of library of utilities

%package -n librp-utils-devel
Summary: Library of utilities, headers and library
Provides:       pkgconfig(librp-utils)
Requires:       librp-utils0
Requires:       librp-utils-headers

%description -n librp-utils-devel
Development files for library of utilities

%package -n librp-utils-static
Summary: Library of utilities, static library
Provides:       pkgconfig(librp-utils-static)
Requires:       librp-utils-headers

%description -n librp-utils-static
Development files for static library of utilities

%prep
%autosetup

%build
%cmake .
%cmake_build

%install
%cmake_install

%files

%files -n librp-utils0
%defattr(-,root,root)
%{_libdir}/librp-utils.so.*

%files -n librp-utils-headers
%defattr(-,root,root)
%dir %{_includedir}/rp-utils
%{_includedir}/rp-utils/*

%files -n librp-utils-devel
%defattr(-,root,root)
%dir %{_includedir}/rp-utils
%{_libdir}/librp-utils.so.0
%{_libdir}/librp-utils.so
%{_libdir}/pkgconfig/librp-utils.pc

%files -n librp-utils-static
%defattr(-,root,root)
%{_libdir}/librp-utils.a
%{_libdir}/pkgconfig/librp-utils-static.pc


%changelog
