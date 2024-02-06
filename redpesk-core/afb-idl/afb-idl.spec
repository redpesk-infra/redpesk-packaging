#---------------------------------------------
# spec file for package afb-idl
#---------------------------------------------

Name:           afb-idl
#Hexsha:        3b7940f36df301e0968fc18d66a5b5fe63b6ddff
Version:        0.4.1
Release:        9%{?dist}
License:        Apache-2.0
Summary:        IDL for micro services
Url:            https://github.com/redpesk-core/afb-idl
Source:         %{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(json-c)
BuildRequires:  flatcc-devel
Requires:       flatcc-devel
Requires:       mustach


%description
IDL for micro services

#---------------------------------------------
%prep
%autosetup -p 1

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
%{_bindir}/afb-genskel
%{_bindir}/afb-exprefs
%{_bindir}/afb-json2c

%{_bindir}/afb-fbgen
%{_libexecdir}/bfbs2json
%{_libexecdir}/jfbsextr
%{_datadir}/afb-idl

#---------------------------------------------
%changelog

* Fri Nov 19 2021 José Bollo jose.bollo@iot.bzh 0.2.0
- [CI] Create MAINTAINERS file
- Add API generation from flatbuffer
- Add CMakeList.txt generation
- Add type params to rpc-type.json generation
- Add afb-fbgen script
- Rename bfbs to flatbuffers
- Add afb-fbgen CMakeList.txt
- Clean up obsolete files
- Add sample directory with custom template example
- Improve afb-fbgen script
- Conditional compilation of afb-fbgen
- Improve generation of binaries
- Prepare Version 0.2
- Fix fb-template typo
- Add jfbsextr for extracting relevant data
- Use jfbsextr in afb-fbgen script
- jfbsextr: Add options
- flatbuffers: Rework templating
