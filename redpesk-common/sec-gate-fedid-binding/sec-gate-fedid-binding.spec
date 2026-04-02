#Archive: None
#Hexsha: 74d622efac8a16340dc84c673c780eaf931e8791
Name:       sec-gate-fedid-binding
Version: 2.0.2
Release: 13%{?dist}
License:    GPL-3.0-only
Summary:    Handle Federerated social-id and local user-id
URL:        https://github.com/redpesk-common/sec-gate-fedid-binding
Source:    %{name}-%{version}.tar.gz

%global _afmappdir %{_prefix}/redpesk

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: sqlite-devel
BuildRequires: pkgconfig(json-c)
BuildRequires: pkgconfig(afb-binding)
BuildRequires: pkgconfig(librp-utils-json-c)
BuildRequires: pkgconfig(sqlite3)

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
%cmake -DAFM_APP_DIR=%{_afmappdir} .
%cmake_build

%install
%cmake_install

%files
%defattr(-,root,root)
%dir %{_afmappdir}
%{_afmappdir}/%{name}
%{_libdir}/libfedid-types.so

%files types-devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc

%clean

%changelog
* Thu Apr 02 2026 José Bollo <jose.bollo@iot.bzh> 2.0.2
- New build dependencies

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

