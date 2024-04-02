
Name: canbus-generator
#Hexsha: 1f63ecfb339487608fb1802d06d2535bb48a99b5
Version: 2.0.0+2+g1f63ecf
Release: 9%{?dist}
Summary: Generate canbus-plugins source files.
Group:          Development/Libraries/C and C++
License: APL2.0
URL: https://github.com/redpesk-common/canbus-generator
Source: %{name}-%{version}.tar.gz

BuildRequires:  afm-rpm-macros
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(canbus-binding) >= 2
BuildRequires:  pkgconfig(afb-binding)
BuildRequires:  pkgconfig(afb-helpers4)
BuildRequires:  pkgconfig(json-c)

%define _afmdatadir %_prefix

%description
%summary

%prep
%autosetup -p 1

%build
%afm_configure_cmake

%make_build -C %{_builddirpkg}


%install
%afm_makeinstall

%check

%clean

%files
%{_bindir}/can-config-generator

%changelog
* Tue Feb 02 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.1+20210129+28+ge7e7ee6
- Upgrade version from source commit sha: e7e7ee6574212b4719f0a829f816248d653f8b52
- Commit message:
- 	[converter]Fix the bit_position_reversed calcul
- 	
- 	The previous one was wrong and could lead to wrong position because of the unsigned cast.
- 	
- 	By example:
- 	
- 	(8*8) - 7 - 64 = -7 --> cast unsigned WRONG
- 	
- 	Change-Id: Iab8c3e43d0271de6d054a2a4d1c668638977e436
- 	Signed-off-by: Clément Benierc <clement.benier@iot.bzh>


* Mon Dec 21 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.1+20201201+27+g32bc633
- Upgrade version from source commit sha: 32bc6338f538d056a6c88e2982cfb054240d1ef8
- Commit message:
- 	Change dependency name
- 	
- 	Signed-off-by: Corentin LE GALL <corentin.legall@iot.bzh>


* Wed Dec 02 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.1+20201201+27+g32bc633
- Upgrade version from source commit sha: 32bc6338f538d056a6c88e2982cfb054240d1ef8
- Commit message:
- 	Change dependency name
- 	
- 	Signed-off-by: Corentin LE GALL <corentin.legall@iot.bzh>


* Fri Nov 27 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.1+20201123+26+g087740e
- Upgrade version from source commit sha: 087740e246d2d1a0e6d4a6a0a91d69d9609ed83c
- Commit message:
- 	main: Fix infinite loop on getopt
- 	
- 	Signed-off-by: Corentin LE GALL <corentin.legall@iot.bzh>


* Mon Oct 19 2020 IoT.bzh <redpesk.list.iot.bzh> 8.0.1
- Creation of the spec file
