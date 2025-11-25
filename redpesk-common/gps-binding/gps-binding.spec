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
#Hexsha: 983cdbc2eb48b8045c31cc89abf8e584762ecd2d
Version: 2.0.0
Release: 16%{?dist}
License: APL2.0
Summary: Gps service set to be used in the redpesk
URL:     https://github.com/redpesk-common/gps-binding
Source: %{name}-%{version}.tar.gz

%global _afmappdir %{_prefix}/redpesk
%global coverage_dir %{_libexecdir}/redtest/%{name}/coverage_data

BuildRequires: cmake
BuildRequires: gcc gcc-c++
BuildRequires: pkgconfig(json-c)
BuildRequires: pkgconfig(afb-binding)
BuildRequires: pkgconfig(afb-helpers4)
BuildRequires: pkgconfig(liburcu)
BuildRequires: pkgconfig(libgps)

Requires: afb-binder

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

%if %{?suse_version} == 1600 || %{?suse_version} == 150600
BuildRequires: libgps30
Requires: libgps30
%endif

%endif


%description
This binding provide a gps service


%package redtest
Summary: redtest package (coverage build)
Requires: lcov
%description redtest
This package contains binaries built with coverage instrumentation.

%prep
%autosetup -p 1

%build
here=$PWD

# Build (no coverage)
mkdir build-no-coverage && cd build-no-coverage
%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DAFM_APP_DIR=%{_afmappdir} \
  -S $here
%cmake_build

# Build coverage (with coverage flags)
cd $here
mkdir build-coverage && cd build-coverage
%cmake \
  -DCMAKE_BUILD_TYPE=Debug \
  -DCMAKE_C_FLAGS="--coverage -fPIC" \
  -DCMAKE_CXX_FLAGS="--coverage -fPIC" \
  -DAFM_APP_DIR=%{coverage_dir} \
  -S $here
%cmake_build
cd $here

%install
here=$PWD

# Install (base package)
cd build-no-coverage
%cmake_install

# Install coverage build (for redtest package)
cd $here
cd build-coverage
%cmake_install

# Copy the coverage files (.gcno) into the coverage_data directory for redtest
find . -name "*.gcno" -exec cp --parents {} %{buildroot}%{coverage_dir}/ \;

# Install redtest scripts (for testing)
cd $here
install -Dm755 redtest/run-redtest %{buildroot}%{_libexecdir}/redtest/%{name}/run-redtest
install -Dm644 test/tests.py %{buildroot}%{_libexecdir}/redtest/%{name}/tests.py
install -Dm644 test/lorient.nmea %{buildroot}%{_libexecdir}/redtest/%{name}/lorient.nmea


%files
%defattr(-,root,root)
%dir %{_afmappdir}
%dir %{_afmappdir}/%{name}
%{_afmappdir}/%{name}/lib/
%{_afmappdir}/%{name}/.rpconfig/


%files redtest
%defattr(-,root,root)
%dir %{_libexecdir}/redtest
%dir %{_libexecdir}/redtest/%{name}
%{_libexecdir}/redtest/%{name}/run-redtest
%{_libexecdir}/redtest/%{name}/tests.py
%{_libexecdir}/redtest/%{name}/lorient.nmea
%{coverage_dir}



%changelog
* Mon Nov 24 2025 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 2.0.0
- refactor of the spec file

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


