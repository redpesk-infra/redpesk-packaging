Name:           redpak-binding
#Hexsha:        b8f7fa4f6788cffa9ad5d6e95eb9b0468307b121
Version:        1.0.0+12+gb8f7fa4
Release: 2%{?dist}
Summary:        This service aims to manage Rednode on target.
Group:          Development/Libraries/C and C++
License:        APL2.0
URL:            https://github.com/redpesk-labs/redpak-binding
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
