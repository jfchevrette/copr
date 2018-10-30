Name:     dunst
Version:  1.3.2
Release:  1%{?dist}
Summary:  Simple and configurable notification-daemon
Group:    User Interface/X
License:  BSD and MIT
URL:      http://www.knopwob.org/dunst
Source0:  https://github.com/dunst-project/dunst/archive/v%{version}.tar.gz

Requires: dbus

BuildRequires: gcc
BuildRequires: glib2-devel
BuildRequires: libX11-devel
BuildRequires: libXinerama-devel
BuildRequires: libXft-devel
BuildRequires: libXScrnSaver-devel
BuildRequires: libxdg-basedir-devel
BuildRequires: libXrandr-devel
BuildRequires: gdk-pixbuf2-devel
BuildRequires: libnotify-devel
BuildRequires: pango-devel
BuildRequires: cairo-devel
BuildRequires: libpng-devel
BuildRequires: dbus-devel
BuildRequires: /usr/bin/pod2man

Provides: desktop-notification-daemon

%description
Dunst is a highly configurable and lightweight notification daemon with the
similar look and feel to dmenu.


%prep
%setup -q


%build
make %{?_smp_mflags} VERSION=%{version} PREFIX=%{_prefix} EXTRACFLAGS="%{optflags}"


%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}


%files
%doc AUTHORS CHANGELOG.md LICENSE README.md
%{_bindir}/%{name}
%{_datadir}/dbus-1/services/org.knopwob.%{name}.service
/usr/lib/systemd/user/dunst.service
%{_datadir}/%{name}
%{_datadir}/man/man1/%{name}.1.gz

%changelog
