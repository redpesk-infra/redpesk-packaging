Name: rp-lib-utils
#Hexsha:    5feeba9a5ff7600487ab3476a315a39efc6f2235
Version: 0.2.0
Release: 28%{?dist}
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

#--------------------------------------------
%package -n librp-utils0
Summary: Library of redpesk C utilities

%description  -n librp-utils0
Development files for static library of utilities

%files -n librp-utils0
%defattr(-,root,root)
%{_libdir}/librp-utils.so.*

%package -n librp-utils-devel
Summary: Library of utilities, headers and library
Provides: pkgconfig(librp-utils)
Requires: librp-utils0
Requires: librp-utils-core-headers
Requires: librp-utils-file-headers
Requires: librp-utils-socket-headers
Requires: librp-utils-json-c-headers
Requires: librp-utils-yaml-headers
Requires: librp-utils-curl-headers

%description -n librp-utils-devel
Development files for library of utilities

%files -n librp-utils-devel
%defattr(-,root,root)
%{_libdir}/librp-utils.so.0
%{_libdir}/librp-utils.so
%{_libdir}/pkgconfig/librp-utils.pc

%package -n librp-utils-static
Summary: Library of utilities, static library
Provides: pkgconfig(librp-utils-static)
Requires: librp-utils-core-headers
Requires: librp-utils-file-headers
Requires: librp-utils-socket-headers
Requires: librp-utils-json-c-headers
Requires: librp-utils-yaml-headers
Requires: librp-utils-curl-headers

%description -n librp-utils-static
Development files for static library of utilities

%files -n librp-utils-static
%defattr(-,root,root)
%{_libdir}/librp-utils.a
%{_libdir}/pkgconfig/librp-utils-static.pc

#--------------------------------------------
%package -n librp-utils-core0
Summary: Library of redpesk C utilities

%description  -n librp-utils-core0
Development files for static library of utilities

%files -n librp-utils-core0
%defattr(-,root,root)
%{_libdir}/librp-utils-core.so.*

%package -n librp-utils-core-devel
Summary: Library of utilities, headers and library
Provides: pkgconfig(librp-utils-core)
Requires: librp-utils-core0
Requires: librp-utils-core-headers

%description -n librp-utils-core-devel
Development files for library of utilities

%files -n librp-utils-core-devel
%defattr(-,root,root)
%{_libdir}/librp-utils-core.so.0
%{_libdir}/librp-utils-core.so
%{_libdir}/pkgconfig/librp-utils-core.pc

%package -n librp-utils-core-static
Summary: Library of utilities, static library
Provides: pkgconfig(librp-utils-core-static)
Requires: librp-utils-headers

%description -n librp-utils-core-static
Development files for static library of utilities

%files -n librp-utils-core-static
%defattr(-,root,root)
%{_libdir}/librp-utils-core.a
%{_libdir}/pkgconfig/librp-utils-core-static.pc

%package -n librp-utils-core-headers
Summary: Headers of library of utilities

%description -n librp-utils-core-headers
Headers of library of utilities

%files -n librp-utils-core-headers
%defattr(-,root,root)
%dir %{_includedir}/rp-utils
%{_includedir}/rp-utils/rp-escape.h
%{_includedir}/rp-utils/rp-jsonstr.h
%{_includedir}/rp-utils/rp-base64.h
%{_includedir}/rp-utils/rp-enum-map.h
%{_includedir}/rp-utils/rp-expand-vars.h
%{_includedir}/rp-utils/rp-pearson.h
%{_includedir}/rp-utils/rp-uuid.h
%{_includedir}/rp-utils/sha1.h
%{_includedir}/rp-utils/rp-verbose.h

#--------------------------------------------
%package -n librp-utils-file0
Summary: Library of redpesk C utilities

%description  -n librp-utils-file0
Development files for static library of utilities

%files -n librp-utils-file0
%defattr(-,root,root)
%{_libdir}/librp-utils-file.so.*

%package -n librp-utils-file-devel
Summary: Library of utilities, headers and library
Provides: pkgconfig(librp-utils-file)
Requires: librp-utils-file0
Requires: librp-utils-file-headers

%description -n librp-utils-file-devel
Development files for library of utilities

%files -n librp-utils-file-devel
%defattr(-,root,root)
%{_libdir}/librp-utils-file.so.0
%{_libdir}/librp-utils-file.so
%{_libdir}/pkgconfig/librp-utils-file.pc

%package -n librp-utils-file-static
Summary: Library of utilities, static library
Provides: pkgconfig(librp-utils-file-static)
Requires: librp-utils-headers

%description -n librp-utils-file-static
Development files for static library of utilities

%files -n librp-utils-file-static
%defattr(-,root,root)
%{_libdir}/librp-utils-file.a
%{_libdir}/pkgconfig/librp-utils-file-static.pc

%package -n librp-utils-file-headers
Summary: Headers of library of utilities

%description -n librp-utils-file-headers
Headers of library of utilities

%files -n librp-utils-file-headers
%defattr(-,root,root)
%dir %{_includedir}/rp-utils
%{_includedir}/rp-utils/rp-file.h
%{_includedir}/rp-utils/rp-path-search.h
%{_includedir}/rp-utils/rp-whichprog.h

#--------------------------------------------
%package -n librp-utils-socket0
Summary: Library of redpesk C utilities

%description  -n librp-utils-socket0
Development files for static library of utilities

%files -n librp-utils-socket0
%defattr(-,root,root)
%{_libdir}/librp-utils-socket.so.*

%package -n librp-utils-socket-devel
Summary: Library of utilities, headers and library
Provides: pkgconfig(librp-utils-socket)
Requires: librp-utils-socket0
Requires: librp-utils-socket-headers

%description -n librp-utils-socket-devel
Development files for library of utilities

%files -n librp-utils-socket-devel
%defattr(-,root,root)
%{_libdir}/librp-utils-socket.so.0
%{_libdir}/librp-utils-socket.so
%{_libdir}/pkgconfig/librp-utils-socket.pc

%package -n librp-utils-socket-static
Summary: Library of utilities, static library
Provides: pkgconfig(librp-utils-socket-static)
Requires: librp-utils-headers

%description -n librp-utils-socket-static
Development files for static library of utilities

%files -n librp-utils-socket-static
%defattr(-,root,root)
%{_libdir}/librp-utils-socket.a
%{_libdir}/pkgconfig/librp-utils-socket-static.pc

%package -n librp-utils-socket-headers
Summary: Headers of library of utilities

%description -n librp-utils-socket-headers
Headers of library of utilities

%files -n librp-utils-socket-headers
%defattr(-,root,root)
%dir %{_includedir}/rp-utils
%{_includedir}/rp-utils/rp-socket.h
%{_includedir}/rp-utils/rp-systemd.h

#--------------------------------------------
%package -n librp-utils-json-c0
Summary: Library of redpesk C utilities

%description  -n librp-utils-json-c0
Development files for static library of utilities

%files -n librp-utils-json-c0
%defattr(-,root,root)
%{_libdir}/librp-utils-json-c.so.*

%package -n librp-utils-json-c-devel
Summary: Library of utilities, headers and library
Provides: pkgconfig(librp-utils-json-c)
Requires: librp-utils-json-c0
Requires: librp-utils-json-c-headers

%description -n librp-utils-json-c-devel
Development files for library of utilities

%files -n librp-utils-json-c-devel
%defattr(-,root,root)
%{_libdir}/librp-utils-json-c.so.0
%{_libdir}/librp-utils-json-c.so
%{_libdir}/pkgconfig/librp-utils-json-c.pc

%package -n librp-utils-json-c-static
Summary: Library of utilities, static library
Provides: pkgconfig(librp-utils-json-c-static)
Requires: librp-utils-headers

%description -n librp-utils-json-c-static
Development files for static library of utilities

%files -n librp-utils-json-c-static
%defattr(-,root,root)
%{_libdir}/librp-utils-json-c.a
%{_libdir}/pkgconfig/librp-utils-json-c-static.pc

%package -n librp-utils-json-c-headers
Summary: Headers of library of utilities

%description -n librp-utils-json-c-headers
Headers of library of utilities

%files -n librp-utils-json-c-headers
%defattr(-,root,root)
%dir %{_includedir}/rp-utils
%{_includedir}/rp-utils/rp-jconf.h
%{_includedir}/rp-utils/rp-jsonc-expand.h
%{_includedir}/rp-utils/rp-jsonc-path.h
%{_includedir}/rp-utils/rp-jsonc.h

#--------------------------------------------
%package -n librp-utils-yaml0
Summary: Library of redpesk C utilities

%description  -n librp-utils-yaml0
Development files for static library of utilities

%files -n librp-utils-yaml0
%defattr(-,root,root)
%{_libdir}/librp-utils-yaml.so.*

%package -n librp-utils-yaml-devel
Summary: Library of utilities, headers and library
Provides: pkgconfig(librp-utils-yaml)
Requires: librp-utils-yaml0
Requires: librp-utils-yaml-headers

%description -n librp-utils-yaml-devel
Development files for library of utilities

%files -n librp-utils-yaml-devel
%defattr(-,root,root)
%{_libdir}/librp-utils-yaml.so.0
%{_libdir}/librp-utils-yaml.so
%{_libdir}/pkgconfig/librp-utils-yaml.pc

%package -n librp-utils-yaml-static
Summary: Library of utilities, static library
Provides: pkgconfig(librp-utils-yaml-static)
Requires: librp-utils-headers

%description -n librp-utils-yaml-static
Development files for static library of utilities

%files -n librp-utils-yaml-static
%defattr(-,root,root)
%{_libdir}/librp-utils-yaml.a
%{_libdir}/pkgconfig/librp-utils-yaml-static.pc

%package -n librp-utils-yaml-headers
Summary: Headers of library of utilities

%description -n librp-utils-yaml-headers
Headers of library of utilities

%files -n librp-utils-yaml-headers
%defattr(-,root,root)
%dir %{_includedir}/rp-utils
%{_includedir}/rp-utils/rp-yaml.h

#--------------------------------------------
%package -n librp-utils-curl0
Summary: Library of redpesk C utilities

%description  -n librp-utils-curl0
Development files for static library of utilities

%files -n librp-utils-curl0
%defattr(-,root,root)
%{_libdir}/librp-utils-curl.so.*

%package -n librp-utils-curl-devel
Summary: Library of utilities, headers and library
Provides: pkgconfig(librp-utils-curl)
Requires: librp-utils-curl0
Requires: librp-utils-curl-headers

%description -n librp-utils-curl-devel
Development files for library of utilities

%files -n librp-utils-curl-devel
%defattr(-,root,root)
%{_libdir}/librp-utils-curl.so.0
%{_libdir}/librp-utils-curl.so
%{_libdir}/pkgconfig/librp-utils-curl.pc

%package -n librp-utils-curl-static
Summary: Library of utilities, static library
Provides: pkgconfig(librp-utils-curl-static)
Requires: librp-utils-headers

%description -n librp-utils-curl-static
Development files for static library of utilities

%files -n librp-utils-curl-static
%defattr(-,root,root)
%{_libdir}/librp-utils-curl.a
%{_libdir}/pkgconfig/librp-utils-curl-static.pc

%package -n librp-utils-curl-headers
Summary: Headers of library of utilities

%description -n librp-utils-curl-headers
Headers of library of utilities

%files -n librp-utils-curl-headers
%defattr(-,root,root)
%dir %{_includedir}/rp-utils
%{_includedir}/rp-utils/rp-curl.h

#--------------------------------------------

%prep
%autosetup

%build
%cmake .
%cmake_build

%install
%cmake_install

%files

%changelog
