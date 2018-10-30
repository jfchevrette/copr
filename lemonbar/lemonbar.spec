%global debug_package %{nil}

Name:           lemonbar
Version:        1.3
Release:        1%{?dist}
Summary:        A featherweight, lemon-scented, bar based on xcb

License:        MIT
URL:            https://github.com/LemonBoy/bar
Source0:        https://github.com/LemonBoy/bar/archive/v%{version}.tar.gz

BuildRequires: gcc
BuildRequires: /usr/bin/pod2man
BuildRequires: libxcb-devel

%description
lemonbar (formerly known as bar) is a lightweight bar entirely based on XCB. Provides full UTF-8 support, basic formatting, RandR and Xinerama support and EWMH compliance without wasting your precious memory.

%prep
%autosetup -n bar-%{version}

%build
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install PREFIX=%{_prefix}


%files
%{_bindir}/lemonbar
%{_mandir}/man1/%{name}.1.gz


%license LICENSE


%changelog
* Fri May 11 2018 Jean-Francois Chevrette <jfchevrette@gmail.com> 1.3-1
- update to 1.3

* Wed Mar 22 2017 Jean-Francois Chevrette <jfchevrette@gmail.com> 1.2-1
- Initial package
