Name:		  rofi
Version:	1.5.1
Release:	1%{?dist}
Summary:	A window switcher, run dialog and dmenu replacement

#Group:		
License:	MIT/X11
URL:		  https://davedavenport.github.io/rofi/
Source0:	https://github.com/DaveDavenport/rofi/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires: pkgconfig(bison)
BuildRequires: pkgconfig(xft) >= 2.0
BuildRequires: pkgconfig(cairo-xcb)
BuildRequires: pkgconfig(check) >= 0.11.0
BuildRequires: pkgconfig(glib-2.0) >= 2.40
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(libstartup-notification-1.0)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xkbcommon) >= 0.5.0
BuildRequires: pkgconfig(xkbcommon-x11)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-xkb)
BuildRequires: pkgconfig(xcb-xinerama)
BuildRequires: pkgconfig(x11-xcb)
BuildRequires: pkgconfig(xcb-util)
BuildRequires: pkgconfig(xcb-ewmh)
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xcb-xrm)


%description
A popup window switcher roughly based on superswitcher, requiring only xlib and pango.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%check
make test

%files
%{_bindir}/rofi
%{_bindir}/rofi-sensible-terminal
%{_bindir}/rofi-theme-selector
%{_includedir}/rofi
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man1/rofi.1.*
%{_mandir}/man1/rofi-sensible-terminal.1.*
%{_mandir}/man5/rofi-theme.5.*
%{_datadir}/rofi/themes/*.rasi
%doc AUTHORS Changelog README.md Examples 
%license COPYING


%changelog
* Thu May 10 2018 Jean-Francois Chevrette <jfchevrette@gmail.com> - 1.5.1
- Updating to version 1.5.1;

* Fri Oct 20 2017 Jean-Francois Chevrette <jfchevrette@gmail.com> - 1.4.2-1
- Updating to version 1.4.2;

* Tue Jan 10 2017 Yaroslav Sapozhnyk <yaroslav.sapozhnik@gmail.com> - 1.3.1-1
- Updating to version 1.3.1;

* Mon Dec 26 2016 Yaroslav Sapozhnyk <yaroslav.sapozhnik@gmail.com> - 1.3.0-1
- Updating to version 1.3.0;

* Fri Aug 26 2016 Yaroslav Sapozhnyk <yaroslav.sapozhnik@gmail.com> - 1.2.0-1
- Updating to version 1.2.0; removed XLib dependency (replaced with
  xcb-util.xrm)

* Wed Jun 15 2016 Yaroslav Sapozhnyk <yaroslav.sapozhnik@gmail.com> - 1.1.0-1
- Updating to version 1.1.0

* Fri Jun 10 2016 Yaroslav Sapozhnyk <yaroslav.sapozhnik@gmail.com> - 1.0.1-1
- Updating to v1.0.1

* Wed Apr 20 2016 Yaroslav Sapozhnyk <yaroslav.sapozhnik@gmail.com> - 1.0.0-1
- Updating to rofi 1.0.0

* Wed Dec 30 2015 Yaroslav Sapozhnyk <yaroslav.sapozhnik@gmail.com> - 0.15.12-1
- Updating to 0.15.12

* Wed Dec 30 2015 Yaroslav Sapozhnyk <yaroslav.sapozhnik@gmail.com> - 0.15.11-2
- Spec file cleanup

* Wed Dec 30 2015 Yaroslav Sapozhnyk <yaroslav.sapozhnik@gmail.com> - 0.15.11-1
- Initial package


