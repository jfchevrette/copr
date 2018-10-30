%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

Name:		sxhkd
Version:	0.5.9
Release:	1%{?dist}
Summary:	Simple X hotkey daemon

License:	BSD
URL:		https://github.com/baskerville/%{name}
# version release
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz
# git release NOTE: comment out macro with `%%` (macros are expanded first)
# Source0:	%%{url}/archive/master.tar.gz

BuildRequires:	gcc
%{?systemd_requires}
BuildRequires:	systemd
BuildRequires:	libxcb-devel
BuildRequires:	xcb-util-devel
BuildRequires:	xcb-util-keysyms-devel

%description
sxhkd is an X daemon that reacts to input events by executing commands.

Its configuration file is a series of bindings that define the associations
between the input events and the commands.

The format of the configuration file supports a simple notation for mapping
multiple shortcuts to multiple commands in parallel.

%prep
## version release
%setup -q
## git release NOTE: comment out macro with `%%` (macros are expanded first)
# %%autosetup -n %{name}-master

%build
%make_build VERBOSE=1 %{?_smp_mflags} CFLAGS="%{optflags}" LDFLAGS="%{?__global_ldflags}"

%install
%make_install PREFIX="%{_prefix}"
install -p -D -m 0644 contrib/systemd/%{name}.service %{buildroot}/%{_unitdir}/%{name}.service

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_docdir}/%{name}/examples
%{_mandir}/man*/%{name}.1.gz
%{_unitdir}/%{name}.service

%changelog
