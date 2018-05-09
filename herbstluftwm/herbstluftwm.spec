Name:           herbstluftwm
Version:        0.7.0
Release:        1%{?dist}
Summary:        A manual tiling window manager
License:        BSD
URL:            http://herbstluftwm.org
Source0:        http://herbstluftwm.org/tarballs/%{name}-%{version}.tar.gz
BuildRequires:  glib2-devel
BuildRequires:  libX11-devel
BuildRequires:  libXinerama-devel

%description
herbstluftwm is a manual tiling window manager for X11 using Xlib and Glib. 
Its main features can be described with:

- The layout is based on splitting frames into subframes which can be split 
again or can be filled with windows;
- Tags (or workspaces or virtual desktops or …) can be added/removed at 
runtime. Each tag contains an own layout exactly one tag is viewed on each 
monitor. The tags are monitor independent;
- It is configured at runtime via ipc calls from herbstclient. So the 
configuration file is just a script which is run on startup.

%package        zsh
Summary:        %{name} zsh completion support
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       zsh

%description    zsh
This package provides zsh completion script of %{name}.

%prep
%setup -q

%build
export CFLAGS+="%{optflags}" CPPFLAGS+="%{optflags}" LDFLAGS="%{__global_ldflags}"
make info
make VERBOSE= %{?_smp_mflags}

%install
make install INSTALL="install -p" PREFIX="%{_prefix}" DESTDIR=%{buildroot} ZSHCOMPLETIONDIR='$(DATADIR)/zsh/site-functions'
# Use %%doc macto to handle docs.
rm -rf %{buildroot}%{_pkgdocdir}
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mv %{buildroot}%{_sysconfdir}/bash_completion.d/herbstclient-completion \
   %{buildroot}%{_datadir}/bash-completion/completions/herbstclient

%files
%doc AUTHORS BUGS LICENSE MIGRATION NEWS
%doc scripts/ doc/*.{html,txt}
%{_sysconfdir}/xdg/%{name}
%{_bindir}/*
%{_datadir}/bash-completion/completions/herbstclient
%{_datadir}/xsessions/%{name}.desktop
%{_mandir}/man1/*.1*
%{_mandir}/man7/*.7* 

%files zsh
%{_datadir}/zsh/site-functions/_herbstclient

%changelog
* Mon Apr 24 2017 Jean-Francois Chevrette <jfchevrette@gmail.com> - 0.7.0-1
- Bump to 0.7.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 11 2014 Christopher Meng <rpm@cicku.me> - 0.6.2-1
- Update to 0.6.2

* Tue Mar 25 2014 Christopher Meng <rpm@cicku.me> - 0.6.1-1
- Update to 0.6.1

* Fri Mar 21 2014 Christopher Meng <rpm@cicku.me> - 0.6.0-1
- Update to 0.6.0

* Fri Dec 27 2013 Christopher Meng <rpm@cicku.me> - 0.5.3-1
- Update to 0.5.3

* Mon Aug 05 2013 Christopher Meng <rpm@cicku.me> - 0.5.2-2
- Move bash completion to better place.

* Mon Aug 05 2013 Christopher Meng <rpm@cicku.me> - 0.5.2-1
- Initial Package.
