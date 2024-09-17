Name:       sec-gate-oidc
#Hexsha:    8b0a98e5d5b0018b9de660a2436de79c164b2aec
Version:    1.0.11
Release:    1%{?dist}
License:    GPLv3
Summary:    secure gateway protecting Websockets API imported through --ws-client=xxx as well as HTML5 or REST page/api serve by afb-binder
URL:        https://github.com/redpesk-common/sec-gate-oidc
Source:     %{name}-%{version}.tar.gz

Requires: sec-gate-fedid-binding-types-devel

BuildRequires: afm-rpm-macros
BuildRequires: sec-gate-fedid-binding-types-devel
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: kernel-headers
BuildRequires: pam-devel
BuildRequires: pcsc-lite-devel
BuildRequires: uthash-devel
BuildRequires: afb-cmake-modules
BuildRequires: pkgconfig(json-c)
BuildRequires: pkgconfig(afb-binding) >= 4.0.1
BuildRequires: pkgconfig(afb-libhelpers) >= 4.0.1
BuildRequires: pkgconfig(libafb) >= 5
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(fedid-types)


BuildRoot:     %{_tmppath}/%{name}-%{version}-build

%description
%summary

%package devel
Requires: %{name} = %{version}
Provides: pkgconfig(%{name}) = %{version}
Summary: %{name} devel

%package sample
Requires: %{name} = %{version}
Summary: %{name} sample

%description devel
sec-sgate-oidc-devel helping developping binding which use the secure gateway

%description sample
Install htdocs files for the secure gate oidc and samples configurations

%files
%afm_files
%exclude %{_afmdatadir}/%{name}/etc/*

%files devel
%afm_files_devel
%{_libdir}/pkgconfig/*
%{_includedir}/*

%files sample
%dir %{_datarootdir}/%{name}
%dir %{_datarootdir}/%{name}/htdocs
%{_datarootdir}/%{name}/htdocs/*
%{_afmdatadir}/%{name}/etc/*

%prep
%autosetup -p 1

%build
%afm_configure_cmake
%afm_build_cmake

%install
%afm_makeinstall
mkdir -p %{buildroot}%{_datarootdir}/%{name}/htdocs
cp -r ./conf.d/project/htdocs/* %{buildroot}%{_datarootdir}/%{name}/htdocs
rm %{buildroot}%{_datarootdir}/%{name}/htdocs/CMake*

%clean

%changelog
* Mon Jul 26 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.0.9+20210723+2+ge8d445b
- Upgrade version from source commit sha: e8d445b348c3730f9183e2c9523255e501659eba
- Commit message:
- 	grammar fix
-
- 	Change-Id: I77044c1c5c63dc9c83e3c90eda1698d72eaca5e4


* Wed Jul 07 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.0.9
- Upgrade version from source commit sha: b05f1f921c0a9de21539f2d9d41489d1d6003ecc
- Commit message:
- 	Fix openSUSE build
-
- 	Signed-off-by: Ronan Le Martret <ronan.lemartret@iot.bzh>


* Fri Jul 02 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.0.9
- Upgrade version from source commit sha: ec244ca8d66a91e455ed7860519df8e7a01f480d
- Commit message:
- 	Fix gcc compilation error due to unitialized pointers
-
- 	[   19s] /home/abuild/rpmbuild/BUILD/sec-gate-oidc-1.0.8/idps/idp-github.c:184:5: error: 'fedUser' may be used uninitialized in this function [-Werror=maybe-uninitialized]
- 	[   19s]      fedUserFreeCB(fedUser);
- 	[   19s]      ^~~~~~~~~~~~~~~~~~~~~~
- 	[   19s] /home/abuild/rpmbuild/BUILD/sec-gate-oidc-1.0.8/idps/idp-github.c:183:5: error: 'fedSocial' may be used uninitialized in this function [-Werror=maybe-uninitialized]
-
- 	Change-Id: Iee38cb629f89f0c2fa05c7c36364589ab273c608
- 	Signed-off-by: Stephane Desneux <stephane.desneux@iot.bzh>


* Wed Jun 30 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.0.8
- Upgrade version from source commit sha: 12c5351b887226c4582a38f4d44e83f78d261fea
- Commit message:
- 	Remove gcc warning format-security
-
- 	Signed-off-by: vlefebvre <valentin.lefebvre@iot.bzh>


* Wed Jun 30 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.0.8
- Upgrade version from source commit sha: 2f5a64a0a568a1b42b9acc4d633e5b2d003f9cab
- Commit message:
- 	Update to libafb 4.0.2


* Wed Jun 30 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.0.8
- Upgrade version from source commit sha: 5760ae9f122685c851e5421e08a77291d17a0a01
- Commit message:
- 	[DOC] correct a 400 Link to docs.onelogin.com
-
- 	Signed-off-by: vlefebvre <valentin.lefebvre@iot.bzh>


* Wed Jun 23 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210623+151742+0+g78302a61
- Upgrade version from source commit sha: 78302a614004baf460035f01460fca0c993ffda2
- Commit message:
- 	[DOC] Adding library pcscd explanation in documentation
-
- 	Signed-off-by: vlefebvre <valentin.lefebvre@iot.bzh>


* Mon Jun 14 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210614+140423+0+geed3a269
- Upgrade version from source commit sha: eed3a2696fd6c4dcdabbe34de814992da97b0164
- Commit message:
- 	Correct default local conf file comments
-
- 	Signed-off-by: vlefebvre <valentin.lefebvre@iot.bzh>


* Mon May 24 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.0.7
- Upgrade version from source commit sha: c1bc44bcd7c0cf4abc55aa5d66c4394505a4e90b
- Commit message:
- 	Changing name of the .extso
-
- 	Signed-off-by: Valentin Lefebvre <valentin.lefebvre@iot.bzh>


* Mon May 24 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.0.7
- Upgrade version from source commit sha: df62cbf6233d4891f458b085662ed8b1af5a89fe
- Commit message:
- 	Adding requires to sec-gate-fedid-binding-devel
-
- 	Signed-off-by: Valentin Lefebvre <valentin.lefebvre@iot.bzh>


* Fri May 21 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.0.6
- Upgrade version from source commit sha: 312a5b32de233f242cd266bb2816604e6e44fec6
- Commit message:
- 	Change project name according to Redpesk Naming
-
- 	Signed-off-by: Valentin Lefebvre <valentin.lefebvre@iot.bzh>


* Thu May 20 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.0.5
- Upgrade version from source commit sha: 312a5b32de233f242cd266bb2816604e6e44fec6
- Commit message:
- 	Change project name according to Redpesk Naming
-
- 	Signed-off-by: Valentin Lefebvre <valentin.lefebvre@iot.bzh>


* Tue May 11 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.0.4
- Upgrade version from source commit sha: 94f72e72b9727a3bc54f23b311b3d2363ac20720
- Commit message:
- 	fix api register uri
-
- 	Signed-off-by: vlefebvre <valentin.lefebvre@iot.bzh>


* Tue May 11 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.0.3
- Upgrade version from source commit sha: c7c8a8dfe4b3d53fa0f19738347deccc7c295e23
- Commit message:
- 	Update pkgconfig file installation
-
- 	Signed-off-by: vlefebvre <valentin.lefebvre@iot.bzh>


* Tue May 11 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.0.2
- Upgrade version from source commit sha: c7c8a8dfe4b3d53fa0f19738347deccc7c295e23
- Commit message:
- 	Update pkgconfig file installation
-
- 	Signed-off-by: vlefebvre <valentin.lefebvre@iot.bzh>


* Tue May 11 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.0.2
- Upgrade version from source commit sha: 88b8243e58d4044ca4aada63a3bbf9985696241f
- Commit message:
- 	Initial generic oidc connector


* Mon May 03 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.0.1
- Upgrade version from source commit sha: 51739ad84956ecc81647262bbf3b85a54026ef91
- Commit message:
- 	Update pkgconfig file installation
-
- 	Signed-off-by: vlefebvre <valentin.lefebvre@iot.bzh>


* Thu Apr 29 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.0.0
- Upgrade version from source commit sha: 51739ad84956ecc81647262bbf3b85a54026ef91
- Commit message:
- 	Update pkgconfig file installation
-
- 	Signed-off-by: vlefebvre <valentin.lefebvre@iot.bzh>


