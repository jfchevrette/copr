Name:           sxhkd
Version:        0.5.9
Release:        1%{?dist}
Summary:        Simple X hotkey daemon

License:        ISC
URL:            https://github.com/baskerville/sxhkd
Source0:        https://github.com/baskerville/sxhkd/archive/%{version}.tar.gz

BuildRequires:  xcb-util-devel
BuildRequires:  xcb-util-keysyms-devel

%description
sxhkd is an X daemon that reacts to input events by executing commands.


%prep
%autosetup


%build
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install PREFIX=%{_prefix}


%files
%{_bindir}/sxhkd
%{_defaultdocdir}/sxhkd
%{_mandir}/man1/sxhkd.1.gz

%license LICENSE
%doc README.md


%changelog
* Mon Aug 21 2017 Jean-Francois Chevrette <jfchevrette@gmail.com> 0.5.8-1
- Update to 0.5.8

* Mon Feb 20 2017 Jean-Francois Chevrette <jfchevrette@gmail.com> 0.5.7-1
- Initial package
