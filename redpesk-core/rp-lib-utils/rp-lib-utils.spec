#Archive: None
#Hexsha: 39ae7a4fa85964442ab3017119d1bc60c3c279d1
Name: rp-lib-utils
Version: 0.3.1
Release: 36%{?dist}
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

# OpenSUSE Leap 16 .a LTO
%global _lto_cflags %{?_lto_cflags} -ffat-lto-objects

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

%post -n librp-utils0 -p /sbin/ldconfig

%postun -n librp-utils0 -p /sbin/ldconfig

%package -n librp-utils-devel
Summary: Library of utilities, headers and library
Requires: librp-utils0
Requires: rp-lib-utils-core-headers
Requires: rp-lib-utils-file-headers
Requires: rp-lib-utils-socket-headers
Requires: rp-lib-utils-json-c-headers
Requires: rp-lib-utils-yaml-headers
Requires: rp-lib-utils-curl-headers

%description -n librp-utils-devel
Development files for library of utilities

%files -n librp-utils-devel
%defattr(-,root,root)
%{_libdir}/librp-utils.so
%{_libdir}/pkgconfig/librp-utils.pc

%package -n librp-utils-static
Summary: Library of utilities, static library
Requires: rp-lib-utils-core-headers
Requires: rp-lib-utils-file-headers
Requires: rp-lib-utils-socket-headers
Requires: rp-lib-utils-json-c-headers
Requires: rp-lib-utils-yaml-headers
Requires: rp-lib-utils-curl-headers

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

%post -n librp-utils-core0 -p /sbin/ldconfig

%postun -n librp-utils-core0 -p /sbin/ldconfig

%package -n librp-utils-core-devel
Summary: Library of utilities, headers and library
Requires: librp-utils-core0
Requires: rp-lib-utils-core-headers

%description -n librp-utils-core-devel
Development files for library of utilities

%files -n librp-utils-core-devel
%defattr(-,root,root)
%{_libdir}/librp-utils-core.so
%{_libdir}/pkgconfig/librp-utils-core.pc

%package -n librp-utils-core-static
Summary: Library of utilities, static library
Requires: rp-lib-utils-core-headers

%description -n librp-utils-core-static
Development files for static library of utilities

%files -n librp-utils-core-static
%defattr(-,root,root)
%{_libdir}/librp-utils-core.a
%{_libdir}/pkgconfig/librp-utils-core-static.pc

%package -n rp-lib-utils-core-headers
Summary: Headers of library of utilities
BuildArch: noarch

%description -n rp-lib-utils-core-headers
Headers of library of utilities

%files -n rp-lib-utils-core-headers
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
%{_includedir}/rp-utils/rp-str2int.h
%{_includedir}/rp-utils/rp-version.h

#--------------------------------------------
%package -n librp-utils-file0
Summary: Library of redpesk C utilities

%description  -n librp-utils-file0
Development files for static library of utilities

%files -n librp-utils-file0
%defattr(-,root,root)
%{_libdir}/librp-utils-file.so.*

%post -n librp-utils-file0 -p /sbin/ldconfig

%postun -n librp-utils-file0 -p /sbin/ldconfig

%package -n librp-utils-file-devel
Summary: Library of utilities, headers and library
Requires: librp-utils-file0
Requires: rp-lib-utils-file-headers

%description -n librp-utils-file-devel
Development files for library of utilities

%files -n librp-utils-file-devel
%defattr(-,root,root)
%{_libdir}/librp-utils-file.so
%{_libdir}/pkgconfig/librp-utils-file.pc

%package -n librp-utils-file-static
Summary: Library of utilities, static library
Requires: rp-lib-utils-file-headers

%description -n librp-utils-file-static
Development files for static library of utilities

%files -n librp-utils-file-static
%defattr(-,root,root)
%{_libdir}/librp-utils-file.a
%{_libdir}/pkgconfig/librp-utils-file-static.pc

%package -n rp-lib-utils-file-headers
Summary: Headers of library of utilities
BuildArch: noarch

%description -n rp-lib-utils-file-headers
Headers of library of utilities

%files -n rp-lib-utils-file-headers
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

%post -n librp-utils-socket0 -p /sbin/ldconfig

%postun -n librp-utils-socket0 -p /sbin/ldconfig

%package -n librp-utils-socket-devel
Summary: Library of utilities, headers and library
Requires: librp-utils-socket0
Requires: rp-lib-utils-socket-headers

%description -n librp-utils-socket-devel
Development files for library of utilities

%files -n librp-utils-socket-devel
%defattr(-,root,root)
%{_libdir}/librp-utils-socket.so
%{_libdir}/pkgconfig/librp-utils-socket.pc

%package -n librp-utils-socket-static
Summary: Library of utilities, static library
Requires: rp-lib-utils-socket-headers

%description -n librp-utils-socket-static
Development files for static library of utilities

%files -n librp-utils-socket-static
%defattr(-,root,root)
%{_libdir}/librp-utils-socket.a
%{_libdir}/pkgconfig/librp-utils-socket-static.pc

%package -n rp-lib-utils-socket-headers
Summary: Headers of library of utilities
BuildArch: noarch

%description -n rp-lib-utils-socket-headers
Headers of library of utilities

%files -n rp-lib-utils-socket-headers
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

%post -n librp-utils-json-c0 -p /sbin/ldconfig

%postun -n librp-utils-json-c0 -p /sbin/ldconfig

%package -n librp-utils-json-c-devel
Summary: Library of utilities, headers and library
Requires: librp-utils-json-c0
Requires: rp-lib-utils-json-c-headers

%description -n librp-utils-json-c-devel
Development files for library of utilities

%files -n librp-utils-json-c-devel
%defattr(-,root,root)
%{_libdir}/librp-utils-json-c.so
%{_libdir}/pkgconfig/librp-utils-json-c.pc

%package -n librp-utils-json-c-static
Summary: Library of utilities, static library
Requires: rp-lib-utils-json-c-headers

%description -n librp-utils-json-c-static
Development files for static library of utilities

%files -n librp-utils-json-c-static
%defattr(-,root,root)
%{_libdir}/librp-utils-json-c.a
%{_libdir}/pkgconfig/librp-utils-json-c-static.pc

%package -n rp-lib-utils-json-c-headers
Summary: Headers of library of utilities
BuildArch: noarch

%description -n rp-lib-utils-json-c-headers
Headers of library of utilities

%files -n rp-lib-utils-json-c-headers
%defattr(-,root,root)
%dir %{_includedir}/rp-utils
%{_includedir}/rp-utils/rp-jconf.h
%{_includedir}/rp-utils/rp-jsonc-expand.h
%{_includedir}/rp-utils/rp-jsonc-default-expand.h
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

%post -n librp-utils-yaml0 -p /sbin/ldconfig

%postun -n librp-utils-yaml0 -p /sbin/ldconfig

%package -n librp-utils-yaml-devel
Summary: Library of utilities, headers and library
Requires: librp-utils-yaml0
Requires: rp-lib-utils-yaml-headers

%description -n librp-utils-yaml-devel
Development files for library of utilities

%files -n librp-utils-yaml-devel
%defattr(-,root,root)
%{_libdir}/librp-utils-yaml.so
%{_libdir}/pkgconfig/librp-utils-yaml.pc

%package -n librp-utils-yaml-static
Summary: Library of utilities, static library
Requires: rp-lib-utils-yaml-headers

%description -n librp-utils-yaml-static
Development files for static library of utilities

%files -n librp-utils-yaml-static
%defattr(-,root,root)
%{_libdir}/librp-utils-yaml.a
%{_libdir}/pkgconfig/librp-utils-yaml-static.pc

%package -n rp-lib-utils-yaml-headers
Summary: Headers of library of utilities
BuildArch: noarch

%description -n rp-lib-utils-yaml-headers
Headers of library of utilities

%files -n rp-lib-utils-yaml-headers
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

%post -n librp-utils-curl0 -p /sbin/ldconfig

%postun -n librp-utils-curl0 -p /sbin/ldconfig

%package -n librp-utils-curl-devel
Summary: Library of utilities, headers and library
Requires: librp-utils-curl0
Requires: rp-lib-utils-curl-headers

%description -n librp-utils-curl-devel
Development files for library of utilities

%files -n librp-utils-curl-devel
%defattr(-,root,root)
%{_libdir}/librp-utils-curl.so
%{_libdir}/pkgconfig/librp-utils-curl.pc

%package -n librp-utils-curl-static
Summary: Library of utilities, static library
Requires: rp-lib-utils-curl-headers

%description -n librp-utils-curl-static
Development files for static library of utilities

%files -n librp-utils-curl-static
%defattr(-,root,root)
%{_libdir}/librp-utils-curl.a
%{_libdir}/pkgconfig/librp-utils-curl-static.pc

%package -n rp-lib-utils-curl-headers
Summary: Headers of library of utilities
BuildArch: noarch

%description -n rp-lib-utils-curl-headers
Headers of library of utilities

%files -n rp-lib-utils-curl-headers
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

* Fri Nov 21 2025 Louis-Baptiste Sobolewski <lb.sobolewski@iot.bzh>
- Update specfile for OpenSUSE Leap 16.0
