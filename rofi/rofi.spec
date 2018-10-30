Name:		  rofi
Version:	1.5.1
Release:	1%{?dist}
Summary:	A window switcher, run dialog and dmenu replacement

#Group:		
License:	MIT/X11
URL:		  https://davedavenport.github.io/rofi/
Source0:	https://github.com/DaveDavenport/rofi/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires: bison
BuildRequires: flex
BuildRequires: gcc
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
%{_mandir}/man1/rofi-theme-selector.1.*
%{_mandir}/man5/rofi-theme.5.*
%{_datadir}/rofi/themes/*.rasi
%doc AUTHORS Changelog README.md Examples 
%license COPYING


%changelog
