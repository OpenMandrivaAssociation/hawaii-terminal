Summary:	Hawaii terminal
Name:		hawaii-terminal
Version:	0.6.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
URL:		http://www.hawaiios.org
Source0:	https://github.com/hawaii-desktop/hawaii-terminal/releases/download/v%{version}/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pam-devel

%track
prog %{name} = {
    url = https://github.com/hawaii-desktop/hawaii-terminal/releases/download/v%{version}/
    regex = "%{name}-(__VER__)\.tar\.xz"
    version = %{version}
}

%description
Hawaii terminal.

%prep
%setup -q

%build
%cmake_qt5
%make

%install
%makeinstall_std -C build

%files
%dir %{_libdir}/qml/Hawaii/Terminal
%{_bindir}/hawaii-terminal
%{_datadir}/applications/hawaii-terminal.desktop
%{_libdir}/qml/Hawaii/Terminal/*
