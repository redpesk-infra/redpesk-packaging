
Name:	cloud-publication-binding
#Hexsha: 2e3f9162c79bcfc91c1e959fc3aa1cf5da0ff006
Version: 2.0.2+20210713+2+g2e3f916
Release: 1%{?dist}
Summary: Cloud Publication Binding
Group: Development/Libraries/C and C++
License: APL2.0
URL: https://github.com/redpesk-common/cloud-publication-binding
Source: %{name}-%{version}.tar.gz

Requires: afb-binder
Requires: redis-tsdb-binding

BuildRequires:  afm-rpm-macros
BuildRequires:	libmicrohttpd-devel >= 0.9.55
BuildRequires:  cmake
BuildRequires:  afb-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(lua) >= 5.3
BuildRequires:  pkgconfig(afb-binding)
BuildRequires:  pkgconfig(afb-libhelpers)
BuildRequires:  pkgconfig(afb-libcontroller)
BuildRequires:  pkgconfig(libsystemd) >= 222

%description
This binding allows to publish redpesk target data to the cloud.

More documentation on the binding and how to use it can be found in the official
redpesk documentation at:
https://docs.redpesk.bzh/docs/en/master/redpesk-core/cloud-pub/1-Architecture.html

%files
%afm_files

%afm_package_devel
%{_libdir}/pkgconfig/*
%{_includedir}/*

%prep
%autosetup -p 1

%build
%afm_configure_cmake
%afm_build_cmake

%install
%afm_makeinstall

%clean

%changelog
* Wed Jul 07 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 2.0.2
- Upgrade version from source commit sha: f0b955f668aa6e2e22558f501af632daaf7c4230
- Commit message:
- 	Main architecture diagram update
- 	
- 	Added an entry for Azure on the cloud side.


* Fri May 21 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 2.0.1
- Upgrade version from source commit sha: 219d5ed07d45dbba5c0ea5faa27d962e329047ce
- Commit message:
- 	Fixed build error seen in Koji/OBS
- 	
- 	The Koji/OBS build environment pass the additional
- 	-Werror=format-security option which was not present in the binding
- 	cmake build rules. This made the build pass in native mode (where only
- 	the binding build rules are used) but fail in Koji/OBS (due to the
- 	differing environment).
- 	
- 	Until both environement are fully unified, this commit adds the
- 	problematic option to the binding build rules so as to get closer to
- 	OBS/Koji. This allows for a better developer experience when building
- 	across environments.
- 	
- 	The code is also updated to fix the actual build issue.


* Wed May 19 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 2.0.0
- Upgrade version from source commit sha: eae5a03b9239d1a30ce29aa762b311e093b4b2bf
- Commit message:
- 	[DOC] Update to use new container installer script
-
- 	This commit updates the binding documentation to follow
- 	modifications done on the container installer script which
- 	now natively supports the cloud publication binding
- 	container.
-


* Tue Apr 06 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.0.2
- Upgrade version from source commit sha: 044f1ff24f39bb9201172bdea68eb86fe8c89b8e
- Commit message:
- 	Followup for localbuilder script rename

- 	Update the doc as the script was renamed.


* Tue Apr 06 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.0.1
- Upgrade version from source commit sha: b5e910d64f054ae3387f65665bc9cce9a77a4050
- Commit message:
- 	[DOC] Update to use new container installer script
-
- 	This commit updates the binding documentation to follow
- 	modifications done on the container installer script which
- 	now natively supports the cloud publication binding
- 	container.


* Fri Apr 02 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.0.0
- Upgrade version from source commit sha: 10f790b13c93c8f40facf3052b6fa3dc6778667c
- Commit message:
- 	First production version of the binding
- 	
- 	This binding allows to selectively publish Redpesk target sensor data to
- 	the cloud. Please see the docs/ directory for more information on how to
- 	use it.
