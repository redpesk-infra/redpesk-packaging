Name:       sec-gate-fedid-binding
#Hexsha: 2c9a061931441acee2f8d30e1d3934e2e50b9103
Version: 1.0.6
Release: 12%{?dist}
License:    GPL-3.0-only
Summary:    Handle Federerated social-id and local user-id
URL:        https://github.com/redpesk-common/sec-gate-fedid-binding
Source:    %{name}-%{version}.tar.gz

BuildRequires: afm-rpm-macros
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: kernel-headers
BuildRequires: sqlite-devel
BuildRequires: afb-cmake-modules
BuildRequires: pkgconfig(json-c)
BuildRequires: pkgconfig(libsystemd) >= 222
BuildRequires: pkgconfig(afb-binding)
BuildRequires: pkgconfig(afb-libhelpers)
BuildRequires: pkgconfig(sqlite3)

BuildRoot:     %{_tmppath}/%{name}-%{version}-build

%description
%summary

%package types-devel
Requires:	%{name} = %{version}
Provides:	pkgconfig(%{name}) = %{version}
Summary: 	Development headers and library for %{name}

%description types-devel
sec-gate-fedid-binding-types-devel is the binding to help developping bindings using federation id

%prep
%autosetup -p 1

%build
%afm_configure_cmake
%afm_build_cmake

%install
%afm_makeinstall

%files
%afm_files
%{_libdir}/*.so

%files types-devel
%afm_files_devel
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc

%clean

%changelog
* Thu May 20 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.0.4
- Upgrade version from source commit sha: d5ea0cc8ab6ab91fc84418ba30095a29ecf74bb4
- Commit message:
- 	Changing name according to the Redpesk naming
- 	
- 	Signed-off-by: Valentin Lefebvre <valentin.lefebvre@iot.bzh>


* Tue May 11 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.0.3
- Upgrade version from source commit sha: 4501bcdffe2e00a380132532fdc790b8b8af5e84
- Commit message:
- 	Adding ld config file
- 	
- 	Signed-off-by: vlefebvre <valentin.lefebvre@iot.bzh>


* Tue May 11 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.0.3
- Upgrade version from source commit sha: 4501bcdffe2e00a380132532fdc790b8b8af5e84
- Commit message:
- 	Adding ld config file
- 	
- 	Signed-off-by: vlefebvre <valentin.lefebvre@iot.bzh>


* Tue May 11 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.0.3
- Upgrade version from source commit sha: 4501bcdffe2e00a380132532fdc790b8b8af5e84
- Commit message:
- 	Adding ld config file
- 	
- 	Signed-off-by: vlefebvre <valentin.lefebvre@iot.bzh>


* Tue May 11 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.0.3
- Upgrade version from source commit sha: 0d5a7f16ba68905abde2fb19d9f782b8d9619674
- Commit message:
- 	Adding ld config file
- 	
- 	Signed-off-by: vlefebvre <valentin.lefebvre@iot.bzh>


* Tue May 11 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.0.2
- Upgrade version from source commit sha: f919485b20500410ba5c16a791e5a695f5a78d7f
- Commit message:
- 	Merge branch 'sandox/valentin/package' into 'master'
- 	
- 	Fix fedid-types.pc.in
- 	
- 	See merge request redpesk/redpesk-common/fedid-binding!1


* Thu Apr 29 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.0.1
- Upgrade version from source commit sha: 4aff1258b1c84b8a74b4ee981aa02808cdd4fcf9
- Commit message:
- 	Fix defid-types.pc.in
- 	
- 	Signed-off-by: vlefebvre <valentin.lefebvre@iot.bzh>


* Tue Apr 27 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.0.0
- Upgrade version from source commit sha: 981c685c5647875d05cf05b15d11d283d1d9a3b3
- Commit message:
- 	Fix check-attrs when pseudo/email exist

