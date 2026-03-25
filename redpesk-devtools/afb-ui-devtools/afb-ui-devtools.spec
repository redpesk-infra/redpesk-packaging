%define debug_package %{nil}

Name: afb-ui-devtools
#Hexsha: 237db174f02f3b6057e8c0e8055217a7d8b4e9bb
Version: 1.0.6
Release: 4%{?dist}
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
local-npm-registry %{_builddir} install --no-optional

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