###########################################################################
# Copyright 2015 - 2020 IoT.bzh
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
###########################################################################
Name:    gps-binding
#Hexsha: e10f2abb1f50c3364f840f12454c95d7f9de7995
Version: 1.1.2
Release: 13%{?dist}
License: GPLv3
Summary: gps api for redpesk
URL:     https://git.ovh.iot/redpesk/redpesk-common/gps-binding
Source: %{name}-%{version}.tar.gz

BuildRequires: afm-rpm-macros
BuildRequires: cmake
BuildRequires: gcc gcc-c++
BuildRequires: afb-cmake-modules
BuildRequires: pkgconfig(json-c)
BuildRequires: pkgconfig(libsystemd) >= 222
BuildRequires: pkgconfig(afb-binding)
BuildRequires: pkgconfig(afb-helpers)
BuildRequires: pkgconfig(liburcu)
BuildRequires: gpsd-devel
Requires: gpsd-devel

%if 0%{?almalinux} == 9
BuildRequires: gpsd-minimal-clients gpsd-minimal
Requires: gpsd-minimal-clients gpsd-minimal
%else
BuildRequires: gpsd-clients gpsd
Requires: gpsd-clients gpsd
%endif

%if 0%{?fedora}
BuildRequires: userspace-rcu-devel
BuildRequires: gpsd-libs
Requires: gpsd-libs
%endif

%if 0%{?suse_version}

%if %sle_version == 150300
BuildRequires: libgps23
Requires: libgps23
%endif

%if %{?suse_version} == 150400
BuildRequires: libgps29
Requires: libgps29
%endif

%endif

%description
The gps api is using gpsd to provide GNSS data.


%afm_package

%afm_package_test

%afm_package_redtest

%prep
%autosetup -p 1

%build
%afm_configure_cmake
%afm_build_cmake

%install
%afm_makeinstall

%check

%clean

%changelog
* Thu Dec 02 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.1.1
- Upgrade version from source commit sha: e10f2abb1f50c3364f840f12454c95d7f9de7995
- Commit message:
- 	Move redtest dir to /usr/libexec and log to /var/log
-
- 	Signed-off-by: Aymeric Aillet <aymeric.aillet@iot.bzh>


* Fri Sep 10 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.1.0
- Upgrade version from source commit sha: 8bff8ce7bdf0f24b0bbe0181cbc85325e5025092
- Commit message:
- 	Enable "is_protected" feature
-
- 	Protected event are immune from deletion.
- 	Bypassing "not_used_count" for these events.
-
- 	Signed-off-by: Aymeric Aillet <aymeric.aillet@iot.bzh>


* Tue Dec 15 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.0.0
- Upgrade version from source commit sha: b9d0d4abb1511711aec012b7b185a512735a83d0
- Commit message:
- 	Fix boolean management
-
- 	Fix error for fedora 33+ based builds
-
- 	Change-Id: Id1fa637e91e4191804ac8f8ef3efb662747ff789
- 	Signed-off-by: Aymeric Aillet <aymeric.aillet@iot.bzh>


* Tue Dec 15 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20201215+115005+0+gb9d0d4ab
- Upgrade version from source commit sha: b9d0d4abb1511711aec012b7b185a512735a83d0
- Commit message:
- 	Fix boolean management
-
- 	Fix error for fedora 33+ based builds
-
- 	Change-Id: Id1fa637e91e4191804ac8f8ef3efb662747ff789
- 	Signed-off-by: Aymeric Aillet <aymeric.aillet@iot.bzh>


* Tue Dec 15 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20201203+155913+0+g9f02ddda
- Upgrade version from source commit sha: 9f02ddda141d2be0fd1b4678e0415bbc8c796897
- Commit message:
- 	Make changes according to new naming convention
-
- 	- Rename every "rp-serice-gps" to "gps-binding" in the projet
- 	- Update dependencies name
- 	- Review specfile
-
- 	Signed-off-by: Corentin LE GALL <corentin.legall@iot.bzh>


