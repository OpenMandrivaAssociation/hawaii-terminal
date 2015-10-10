Summary:	Hawaii terminal
Name:		hawaii-terminal
Version:	0.5.91
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
URL:		http://www.maui-project.org
Source0:	https://github.com/hawaii-desktop/hawaii-terminal/releases/download/v%{version}/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	qt5-devel

%track
prog %{name} = {
    url = http://downloads.sourceforge.net/project/mauios/hawaii/
    regex = "%{name}-(__VER__)\.tar\.gz"
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
%{_bindir}/hawaii-terminal
%{_datadir}/applications/hawaii-terminal.desktop
