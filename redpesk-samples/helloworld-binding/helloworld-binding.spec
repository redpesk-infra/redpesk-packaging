###########################################################################
# Copyright 2015 - 2022 IoT.bzh
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

Name:    helloworld-binding
#Hexsha: 3e17e7a444ada20ea766ee902ede234fc768edae
Version: 1.1.1
Release: 4%{?dist}
License: MIT
Summary: Helloworld service set to be used in redpesk
URL:     https://github.com/redpesk-samples/helloworld-binding
Source:  %{name}-%{version}.tar.gz

Requires: afb-binder

BuildRequires: afm-rpm-macros
BuildRequires: cmake
BuildRequires: gcc gcc-c++
BuildRequires: afb-cmake-modules >= 10.0.8
BuildRequires: pkgconfig(json-c)
BuildRequires: pkgconfig(libsystemd) >= 222
BuildRequires: pkgconfig(afb-binding)
BuildRequires: pkgconfig(afb-libhelpers)

%description
The helloworld agl service gathers two bindings.
- helloworld-skeleton: Increment a counter
- helloworld-subscribe-event: Subscribe and get notified whether an event is emited

# main package: default install in /var/local/lib/afm/applications/%%{name}
%afm_package

# test package: default install in /var/local/lib/afm/applications/%%{name}-test
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

* Tue May 16 2023 José Bollo jose.bollo@iot.bzh 1.0.2
Fix debian packaging
* Thu Feb 10 2022 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.0.1+20220119+7+gb698cc6
- Upgrade version from source commit sha: b698cc60aeddb65884b6b04e4f81ecc63e487290
- Commit message:
- 	Update autobuild for linux
- 	
- 	Signed-off-by: Ronan Le Martret <ronan.lemartret@iot.bzh>



* Fri Dec 11 2020 IoT.bzh <armand.beneteau.iot.bzh> 8.99.7
- Adaptation for RedPesk 33

* Wed Jun 24 2020 IoT.bzh <armand.beneteau.iot.bzh> 8.99.6
- Add the use of cmake template for run-redtest

* Mon May 18 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> gcde438ae
- Upgrade version from source commit sha: cde438aed1e990b69d4ed2fb3aa3b4ba22e78a6a
- Commit message:
- 	Correction inside the run-redtest script (#3)
-

* Mon May 18 2020 IoT.bzh <clement.benier@iot.bzh> 8.99.6
- bump version of afm-rpm-macros

* Wed Apr 29 2020 IoT.bzh <redpesk.list.iot.bzh> 8.99.6
- Modifications in order to add a redtest subpackage

* Wed Feb 19 2020 IoT.bzh <redpesk.list.iot.bzh> 8.99.5
- Modifications in order to add a test subpackage

* Fri Feb 14 2020 IoT.bzh <redpesk.list.iot.bzh> 8.99.5
- Creation of the spec file from RedPesk generator
