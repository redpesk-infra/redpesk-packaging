%define         debug_package %{nil}
Name: 	        signal-composer-binding
#Hexsha: 92eed99ad927ce6e46bcdee336830d71ee8df41f
Version: 1.0.1
Release: 5%{?dist}
Summary:        Signal composer API connected to low level AGL services
Group:          Development/Libraries/C and C++
License: 	    APL2.0
URL: 	        http://git.ovh.iot/redpesk/redpesk-common/signal-composer-binding
Source:         %{name}-%{version}.tar.gz

Requires:       afb-binder

BuildRequires:  afm-rpm-macros
BuildRequires:  cmake
BuildRequires:  afb-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kernel-headers
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(lua) >= 5.3
BuildRequires:  pkgconfig(afb-binding)
BuildRequires:  pkgconfig(afb-helpers)
BuildRequires:  pkgconfig(appcontroller)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(libsystemd) >= 222

%if 0%{?suse_version}
%define build_ldflags -Wl,--no-as-needed -ldl -Wl,--no-as-needed -lsystemd
%endif

%description
signal-composer level binding

Summary: %{name}

%files
%afm_files

%afm_package_devel
%{_includedir}/*
%{_libdir}/pkgconfig/*

%prep
%autosetup -p 1

%build
%afm_configure_cmake  \
%if 0%{?suse_version}
 -DCMAKE_EXE_LINKER_FLAGS="%{?build_ldflags} -Wl,--as-needed -Wl,-z,now"\
 -DCMAKE_SHARED_LINKER_FLAGS="%{?build_ldflags} -Wl,--as-needed -Wl,-z,now"
%endif

%afm_build_cmake

%install
%afm_makeinstall

%check

%clean

%changelog
* Mon Jun 07 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.0.0
- Upgrade version from source commit sha: 849103f5ba8d2a998889899ec82e614df7e5bd4b
- Commit message:
- 	[signal]Remove compile warning
- 	
- 	/home/devel/gitsources/gitlab/redpesk/redpesk-common/signal-composer-binding/signal-composer-binding/signal.hpp:65:15: warning: ‘Signal::metadata_’ will be initialized after [-Wreorder]
- 	  json_object* metadata_;
- 	               ^~~~~~~~~
- 	/home/devel/gitsources/gitlab/redpesk/redpesk-common/signal-composer-binding/signal-composer-binding/signal.hpp:57:14: warning:   ‘CtlActionT* Signal::onReceived_’ [-Wreorder]
- 	  CtlActionT* onReceived_;
- 	
- 	Change-Id: I1e9c642ba0b10d773b13c4bffdeb09dacd0a7675
- 	Signed-off-by: Romain Forlot <romain.forlot@iot.bzh>


* Thu Dec 17 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 10.0.4
- Upgrade version from source commit sha: 8f520043ef785b19e13da3ee35f4054e99c03a19
- Commit message:
- 	[.pc.in] Tweak dependance name
- 	
- 	Debian likes build did not find the appcontroller dependance
- 	since it has been renamed from appcontroller to afb-libcontroller
- 	
- 	Signed-off-by: Marc-Antoine Riou <marc-antoine.riou@iot.bzh>


* Tue Dec 15 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 10.0.3+20201215+1+g6431dcb
- Upgrade version from source commit sha: 6431dcb7c1d48c67b0f2626a74d01e93dab439c1
- Commit message:
- 	[config.xml] Fill it with cmake variables
-
- 	Signed-off-by: Marc-Antoine Riou <marc-antoine.riou@iot.bzh>


* Tue Dec 15 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 10.0.3
- Upgrade version from source commit sha: 0099281dc065f1ef21210e0bfd12a379a2d63bb6
- Commit message:
- 	[verbInfo] tweak the response structure to match ui expectations
-
- 	Signed-off-by: Marc-Antoine Riou <marc-antoine.riou@iot.bzh>


* Sun Dec 13 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 10.0.2
- Upgrade version from source commit sha: b8461a807cdeb04c87adde1697060e7ad93893b0
- Commit message:
- 	[config.xml] change the entry point
-
- 	The binding name has recently changed from "afb-signal-composer" to "afb-signal-composer-binding".
- 	Report this change in the config.xml
-
- 	Signed-off-by: Marc-Antoine Riou <marc-antoine.riou@iot.bzh>


* Fri Dec 11 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 10.0.1
- Upgrade version from source commit sha: 3d532d5efb2f34bdf2234af22669c07b0132bf5b
- Commit message:
- 	[verb info] increment the json counter when invoked
-
- 	The reference counter of the info response was set to 0 after the first call. It ends up in a segmentation fault after each new call.
-
- 	Signed-off-by: Marc-Antoine Riou <marc-antoine.riou@iot.bzh>


* Thu Dec 10 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 10.0.0
- Upgrade version from source commit sha: eb5b177a644b945430ab3923a414e3f48f46f353
- Commit message:
- 	[config.xml] Update the binding configuration
-
- 	update the low-can dependency: low-can -> canbus
- 	add a dependency for demo purpose: redis
-
- 	Signed-off-by: Marc-Antoine Riou <marc-antoine.riou@iot.bzh>


* Thu Dec 10 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.1+20201210+34+geb5b177
- Upgrade version from source commit sha: eb5b177a644b945430ab3923a414e3f48f46f353
- Commit message:
- 	[config.xml] Update the binding configuration
-
- 	update the low-can dependency: low-can -> canbus
- 	add a dependency for demo purpose: redis
-
- 	Signed-off-by: Marc-Antoine Riou <marc-antoine.riou@iot.bzh>


* Thu Dec 10 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 10.0.0
- Upgrade version from source commit sha: 4bd68f85e1e79242d55d0cbea8cae4d3f3654b9b
- Commit message:
- 	[install header] deploy every headers in devel package
-
- 	append to the list of headers the last two that were missing.
-
- 	Signed-off-by: Marc-Antoine Riou <marc-antoine.riou@iot.bzh>


* Wed Dec 09 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.1+20201208+35+g4bd68f8
- Upgrade version from source commit sha: 4bd68f85e1e79242d55d0cbea8cae4d3f3654b9b
- Commit message:
- 	[install header] deploy every headers in devel package
-
- 	append to the list of headers the last two that were missing.
-
- 	Signed-off-by: Marc-Antoine Riou <marc-antoine.riou@iot.bzh>


* Wed Dec 09 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.1+20201126+2+g470ac44
- Upgrade version from source commit sha: 470ac44d0184422ae9ba84a25b2ee8368abdd40a
- Commit message:
- 	Merge branch 'improvement' into 'master'
-
- 	Fix binding specific issue
-
- 	See merge request redpesk/redpesk-common/signal-composer-binding!1


* Tue Dec 08 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.1+20201208+34+g36df9ee
- Upgrade version from source commit sha: 36df9ee5bdb67524e4e49dcb2f080aa657a70e4f
- Commit message:
- 	[config.cmake] rename afb-daemon dependency
-
- 	Signed-off-by: marco <marc-antoine.riou@iot.bzh>


* Tue Dec 08 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.1+20201208+33+gf47cf0b
- Upgrade version from source commit sha: f47cf0bb5f50154a553f245f2efaecd949a82071
- Commit message:
- 	[config.cmake] tweak pkg name for controller & afb-helpers
-
- 	Signed-off-by: Marc-Antoine Riou <marc-antoine.riou@iot.bzh>


