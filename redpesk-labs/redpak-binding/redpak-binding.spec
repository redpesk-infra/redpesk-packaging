Name:           redpak-binding
#Hexsha:        c8dd4244fdb5a6588d890797f34dc444f6ded9fe
Version:        1.0.0+20220804+5+gc8dd424
Release: 1%{?dist}
Summary:        This service aims to manage Rednode on target.
Group:          Development/Libraries/C and C++
License:        APL2.0
URL:            http://git.ovh.iot/redpesk/redpesk-labs/redpak-binding.git
Source:         %{name}-%{version}.tar.gz

BuildRequires:  afm-rpm-macros
BuildRequires:  cmake
BuildRequires:  afb-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  userspace-rcu-devel
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(afb-binding)
BuildRequires:  pkgconfig(afb-libhelpers)
BuildRequires:  pkgconfig(red-pak)

Requires: afb-binder

%description
%summary

%prep
%autosetup -p 1

%build
%afm_configure_cmake

%make_build -C %{_builddirpkg}
make widget_files -C %{_builddirpkg}

%install
%afm_makeinstall

%files
%afm_files

%changelog