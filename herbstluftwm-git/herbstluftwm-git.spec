%define commit0 aed40ff791e23213f94be6f461e3da4753b9e458
%define shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%define timestamp %(date +"%Y%m%d%H%M")

Name:           herbstluftwm-git
Version:        0.7.0
Release:        1.%{timestamp}git%{shortcommit0}%{?dist}
Summary:        A manual tiling window manager
License:        BSD
URL:            https://github.com/herbstluftwm/herbstluftwm/
Source0:        https://github.com/herbstluftwm/herbstluftwm/archive/%{shortcommit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires:  asciidoc
BuildRequires:  glib2-devel
BuildRequires:  libX11-devel
BuildRequires:  libXinerama-devel

Conflicts:      herbstluftwm

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

%package        fish
Summary:        %{name} fish completion support
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       fish

%description    fish
This package provides fish completion script of %{name}.

%prep
%autosetup -n herbstluftwm-%{commit0}  
#%setup -q

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
%{_sysconfdir}/xdg/herbstluftwm
%{_bindir}/*
%{_datadir}/bash-completion/completions/herbstclient
%{_datadir}/xsessions/herbstluftwm.desktop
%{_docdir}/*
%{_mandir}/man1/*.1*
%{_mandir}/man7/*.7*

%files zsh
%{_datadir}/zsh/site-functions/_herbstclient

%files fish
%{_datadir}/fish/vendor_completions.d/herbstclient.fish

%changelog
* Wed May 24 2017 Jean-Francois Chevrette <jfchevrette@gmail.com> - f629fb6
- Initial Package from git.
