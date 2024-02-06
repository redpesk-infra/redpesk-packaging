%define debug_package %{nil}

Name:sec-gate-webui
#Hexsha: d09667950cff935b34bd96d7dc4fb0e9229af23f
Version: 1.0.0
Release: 1%{?dist}
Summary: Web interface for the secure gateway
License: AFL-2.0
Group:   Development/Tools/Other
Url:     https://github.com/redpesk-common/sec-gate-webui
Source0: %{name}-prebuild-%{version}.tar.gz

BuildRequires:  fdupes

Requires:       afb-binder

BuildArch:      noarch


%description
This is %{summary}.

%files
%dir %{_datarootdir}/sec-gate-webui
%{_datarootdir}/sec-gate-webui/

%prep
%setup -n %{name}-prebuild-%{version}

%build

%install
mkdir -p %{buildroot}%{_datarootdir}/sec-gate-webui
#cp -R %{_builddir}/*/sec-gate-webui-1.0.0/* %{buildroot}%{_datarootdir}/sec-gate-webui
cp -r ./* %{buildroot}%{_datarootdir}/sec-gate-webui

%check

%clean

%changelog
* Fri Jul 23 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.0.0
- Upgrade version from source commit sha: d09667950cff935b34bd96d7dc4fb0e9229af23f
- Commit message:
- 	Initial commit
- 	
- 	Signed-off-by: vlefebvre <valentin.lefebvre@iot.bzh>


* Fri Jul 23 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 0.0.0+20210723+162452+0+gd0966795
- Upgrade version from source commit sha: d09667950cff935b34bd96d7dc4fb0e9229af23f
- Commit message:
- 	Initial commit
- 	
- 	Signed-off-by: vlefebvre <valentin.lefebvre@iot.bzh>


* Wed Jun 30 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.0.0
- Upgrade version from source commit sha: 33debc6bc291965f2c9843225682122acfd9cc64
- Commit message:
- 	Merge branch 'sandbox/rodrigo/router-test' into 'master'
- 	
- 	[CHANGE] Angular version & new url routing with #
- 	
- 	See merge request redpesk/redpesk-common/afb-oidc-web-tool!1
