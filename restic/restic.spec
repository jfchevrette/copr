Name:           restic
Version:        0.8.3
Release:        1%{?dist}
Summary:        Fast, secure, efficient backup program

License:        BSD 2-clause
URL:            https://restic.github.io/
Source0:        https://github.com/restic/restic/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: golang

%define debug_package %{nil}

%description
restic is a backup program that is fast, efficient and secure.

%prep
%autosetup

%build
go run build.go

%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 %{_builddir}/%{name}-%{version}/%{name} %{buildroot}/%{_bindir}

%files
%{_bindir}/%{name}


%changelog
* Thu May 10 2018 Jean-Francois Chevrette <jfchevrette@gmail.com> 0.8.3
- update to 0.8.3

* Mon Feb 19 2018 Jean-Francois Chevrette <jfchevrette@gmail.com> 0.8.2
- update to 0.8.2

* Mon Nov 27 2017 Jean-Francois Chevrette <jfchevrette@gmail.com> 0.8.0
- update to 0.8.0

* Thu Sep 22 2017 Jean-Francois Chevrette <jfchevrette@gmail.com> 0.7.3
- update to 0.7.3

* Wed Aug 2 2017 Jean-Francois Chevrette <jfchevrette@gmail.com> 0.7.0
- update to 0.7.1

* Thu Jun 29 2017 Jean-Francois Chevrette <jfchevrette@gmail.com> 0.6.1
- Initial package
