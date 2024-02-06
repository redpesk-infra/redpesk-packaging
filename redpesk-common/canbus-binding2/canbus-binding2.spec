Name: canbus-binding2
%global _name      canbus-binding
%global _afmappdir %{_prefix}/redpesk

#Hexsha: b16677ba63b4daf5ce53577bb3713d7368ceb3bb
Version: 2.0.3
Release: 5%{?dist}
Summary: Signal composer API connected to low level AGL services
Group:   Development/Libraries/C and C++
License: APL2.0
URL: http://git.ovh.iot/redpesk/redpesk-common/canbus-binding.git
Source: %{name}-%{version}.tar.gz

Conflicts: %{_name}

Recommends: afb-app-manager
Requires: afb-binder

BuildRequires:  cmake
BuildRequires:  afb-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kernel-headers
BuildRequires:  afb-idl
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(afb-binding)
BuildRequires:  pkgconfig(librp-utils)
BuildRequires:  pkgconfig(afb-helpers4)

%description
Canbus level binding 2

%{summary}

%package devel
Requires: %{name} = %{version}
Provides: pkgconfig(%{_name}) = %{version}
Summary:  %{summary} (development package)

%description devel 
%summary 
This is the development package for %{_name} 2.


%package plugin-template
Summary: %{name} plugin-template
Requires: %{name} = %{version}

%description plugin-template
A template to make plugins for the %{name}.


%prep
%autosetup -p 1 -n %{name}-%{version}

%build
%cmake .  -DAFM_APP_DIR=%{_afmappdir}
%cmake_build


%install
%cmake_install

%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%files
%dir %{_afmappdir}
%dir %{_afmappdir}/%{_name}
%{_afmappdir}/%{_name}
%{_libdir}/libcanbus.so.*

%files devel
%dir %{_libdir}/pkgconfig
%{_libdir}/libcanbus.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%dir %{_datadir}/%{_name}
%{_datadir}/%{_name}/docs

%files plugin-template
%dir %{_datadir}/%{_name}
%{_datadir}/%{_name}/plugin_template


%check

%clean

%changelog

* Wed Sep 06 2023 José Bollo jose.bollo@iot.bzh 2.0.0
- new 2.0.0 packaging

* Mon Jan 23 2023 José Bollo jose.bollo@iot.bzh 1.1.1
- Change the packaging of the development
- Bump version 1.1.1
* Mon Jun 07 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 1.0.0
- Upgrade version from source commit sha: b2c3138a47278872497ffafcac34753908d9dbee
- Commit message:
- 	[all]Rename attribute generic_name_ to name_
-
- 	This is the continuation of the simplification of signal name by removing the prefix and only use 1 name
- 	instead of 2: 1 name And Prefix + Name
-
- 	Change-Id: I40954d318608a01e052fdd467b0e810820e5e24c
- 	Signed-off-by: Romain Forlot <romain.forlot@iot.bzh>


* Wed Apr 14 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.2
- Upgrade version from source commit sha: f19eee27fabd51c70bbafcdc4922318afcc6cdfc
- Commit message:
- 	Add create can socket permission in config.xml
-
- 	The binding will be allowed to create can socket
- 	in its selinux rules. (sec-lsm-manager)
-
- 	Signed-off-by: Arthur Guyader <arthur.guyader@iot.bzh>
- 	Change-Id: I86649e850a7b24780e9b6a685d5a4aff536b0eec


* Tue Dec 22 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.1+20201222+6+g2a919fc
- Upgrade version from source commit sha: 2a919fc81a67020dd69b7c410c2d2cd8eeb98a42
- Commit message:
- 	[rpath] Remove RPATH and add config file
-
- 	- Remove RPATH from cmake and add a config file for ld that
- 	will in installed in /etc/ld.so.conf.d/
-
- 	Signed-off-by: Corentin LE GALL <corentin.legall@iot.bzh>


* Tue Dec 22 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.1+20201211+5+g0eda2ae
- Upgrade version from source commit sha: 0eda2ae2c249df4f3d190d48ca7103d641b9ee2f
- Commit message:
- 	[binding]Ignore if add_verb call fails.
-
- 	Adding a verb based on the signal name could end up to a failure because of 2 signals using
- 	the same name. This lets ignore the problem and goes on.
-
- 	Change-Id: If30342db3cddc00ef06cdf5e5fc0f75f63bbd1cd
- 	Signed-off-by: Romain Forlot <romain.forlot@iot.bzh>


* Thu Dec 10 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.1+20201209+4+gdfed29c
- Upgrade version from source commit sha: dfed29c19eb58e630307a38e6e0ee9227ed9af1f
- Commit message:
- 	[signal/binding]Chg dedicated signal verb behavior
-
- 	Now get 1 verb/signal with different action depending on the arguement provided.
- 	At the moment, the privilege check is made on a permission text.
- 	Add the ability to retrieve the shared_ptr of the signal object from the object itself
- 	easier than juste rebuild a make_shared each time.
-
- 	Make some cleanup on old separated 4 verbs per signal and add a wrapper one to call
- 	them all, get, write, subscribe, unsubscribe.
-
- 	Change-Id: I00e35a8fae0f9ac68f10aeb515b008884a8cfa3e
- 	Signed-off-by: Romain Forlot <romain.forlot@iot.bzh>


* Tue Dec 08 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.1+20201207+3+g2532477
- Upgrade version from source commit sha: 2532477f80596339e67eaa7399b8a1b3a7f914e4
- Commit message:
- 	[verbname] allow every char for signal verbs name
-
- 	Some PGN name contain the same letters but different digits in their names.
- 	The canbus binding replaced every char excepting letters by a "_".
- 	This implies multiple verbs definition with the same name, and so the canbus crashed.
-
- 	Because the application framework allows any char to be in verb name, the canbus accept it too.
-
- 	Signed-off-by: Marc-Antoine Riou <marc-antoine.riou@iot.bzh>


* Mon Dec 07 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.1+20201207+2+gc4faa17
- Upgrade version from source commit sha: c4faa17e532ec9398f5025995fdf083304c1e528
- Commit message:
- 	Change afb-helpers and appcontroller to real name
-
- 	Signed-off-by: Corentin LE GALL <corentin.legall@iot.bzh>


* Fri Dec 04 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.1+20201204+1+g7c0f2b3
- Upgrade version from source commit sha: 7c0f2b31e50e17d28a09906efdf8967ceaa12cd0
- Commit message:
- 	Adjust name of copyright owner
-
- 	Signed-off-by: Corentin LE GALL <corentin.legall@iot.bzh>


* Thu Dec 03 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 8.0.1+20201203+243+gea579b7
- Upgrade version from source commit sha: ea579b7f65a265b6e8fa18b7bd83a451544d37ca
- Commit message:
- 	Update plugins-template's CMakeLists
-
- 	Signed-off-by: Corentin LE GALL <corentin.legall@iot.bzh>


* Tue Dec 01 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 8.0.1+20201201+242+g028ebd9
- Upgrade version from source commit sha: 028ebd960424526a028d74d53ec79fa3bdcccf9a
- Commit message:
- 	Merge branch 'sandbox/corentin/rename/doc_api_bin' into 'master'
-
- 	Sandbox/corentin/rename/doc api bin
-
- 	See merge request redpesk/redpesk-common/canbus-binding!15


* Mon Nov 30 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 8.0.1+20201127+237+g50bbb9d
- Upgrade version from source commit sha: 50bbb9d9b092eebe94a40e3fd587f5a176d34dce
- Commit message:
- 	Fix change afb-daemon name to afb-binding
-
- 	Change-Id: I602eaac62e4b24afe7377ab9eb559796e68d604e
- 	Signed-off-by: Romain Forlot <romain.forlot@iot.bzh>

