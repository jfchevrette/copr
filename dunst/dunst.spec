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
* Thu Feb 08 2018 Jean-Francois Chevrette <jfchevrette@gmail.com> 1.3.1-1
- Removed numlock patch
- Bump to version 1.3.1

* Tue Jun 03 2014 Lukas Zapletal <lzap+rpm@redhat.com> 1.0.0-3
- Backported numlock fix (RHBZ 1103216)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat May 11 2013 Lukas Zapletal <lzap+rpm[@]redhat.com> - 1.0.0-1
- bump to stable version 1.0.0

* Mon Jan 28 2013 Lukas Zapletal <lzap+rpm[@]redhat.com> - 0.5.0-1
- version bump
- inih library is no longer required

* Mon Sep 03 2012 Lukas Zapletal <lzap+rpm[@]redhat.com> - 0.3.1-3
- package review

* Wed Aug 29 2012 Lukas Zapletal <lzap+rpm[@]redhat.com> - 0.3.1-2
- package review

* Mon Aug 27 2012 Lukas Zapletal <lzap+rpm[@]redhat.com> - 0.3.1-1
- initial version
