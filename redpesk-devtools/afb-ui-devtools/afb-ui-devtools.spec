#Archive: afb-ui-devtools-1.1.0.tar.gz
#Hexsha: e497291a709d3f855cfe1b7e14afb23a5905abc7
%define debug_package %{nil}

Name: afb-ui-devtools
Version: 1.1.0
Release: 5%{?dist}
Summary: Web interface for the binder
License: AFL-2.0
Group:   Development/Tools/Other
Url:     https://github.com/redpesk-devtools/afb-ui-devtools
Source0: %{name}-%{version}.tar.gz
Source1: vendor_node.cpio
Buildarch: noarch

BuildRequires:  jq
BuildRequires:  npm
BuildRequires:  nodejs
BuildRequires:  nodejs-full-i18n
BuildRequires:  local-npm-registry

Requires:       afb-binder

%description
This is %{summary}.

%files
%dir %{_datarootdir}/afb-ui-devtools
%{_datarootdir}/afb-ui-devtools/

%prep
cpio -i < %{SOURCE1}
%setup -n %{name}-%{version}
local-npm-registry %{_builddir} install --legacy-peer-deps

%build
npm run build:prod

%install
mkdir -p %{buildroot}%{_datarootdir}/afb-ui-devtools/binder
cp -r dist/* %{buildroot}%{_datarootdir}/afb-ui-devtools/binder

%check

%clean

%changelog
* Fri Mar 19 2021 IoT.bzh <redpesk.list.iot.bzh> 1.0.4
- Fix wss support
* Wed Mar 10 2021 IoT.bzh <redpesk.list.iot.bzh> 1.0.3
- Add disconnect button and alerts
- Fix prod/debug connection and cleanup useless code
- Fix license header, packaging and linter error
* Thu Dec 01 2020 IoT.bzh <redpesk.list.iot.bzh> 1.0.2
- Creation of the spec file