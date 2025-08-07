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

Name:    wifiap-binding
#Hexsha: 11e8858c5c718e26d2276c22b5c6237aba00693a
Version: 0.1.3
Release: 16%{?dist}
License: GPLv3
Summary: wifi access point api for redpesk
URL:     http://git.ovh.iot/redpesk/redpesk-common/wifiap-binding
Source0: %{name}-%{version}.tar.gz

%global _afmappdir %{_prefix}/redpesk

BuildRequires: cmake
BuildRequires: gcc gcc-c++
BuildRequires: afb-cmake-modules
BuildRequires: pkgconfig(json-c)
BuildRequires: pkgconfig(libsystemd) >= 222
BuildRequires: pkgconfig(afb-binding)
BuildRequires: pkgconfig(libmicrohttpd) >= 0.9.55
BuildRequires: pkgconfig(afb-helpers)
BuildRequires: pkgconfig(liburcu)
BuildRequires: pkgconfig(afb-libcontroller)
Requires: afb-binder hostapd dnsmasq

%description
The wifiap api is using hostapd to generate a wifi access point.

%prep
%autosetup -p 1

%build
%cmake . -DAFM_APP_DIR=%{_afmappdir}
%cmake_build

%install
%cmake_install

%check

%clean

%files
%dir %{_afmappdir}
%{_afmappdir}/%{name}

%changelog

