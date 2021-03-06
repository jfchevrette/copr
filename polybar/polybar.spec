Name: polybar
Version: 3.2.1
Release: 1%{?dist}
Summary: A fast and easy-to-use tool for creating status bars
License: MIT
URL: https://github.com/jaagr/polybar

BuildRequires: alsa-lib-devel
BuildRequires: binutils
BuildRequires: cairo-devel
BuildRequires: clang
BuildRequires: cmake
BuildRequires: cmake-data
BuildRequires: git
BuildRequires: i3
BuildRequires: jsoncpp-devel
BuildRequires: libcurl-devel
BuildRequires: libmpdclient-devel
BuildRequires: libxcb-devel
BuildRequires: python2
BuildRequires: wireless-tools-devel
BuildRequires: xcb-proto
BuildRequires: xcb-util-image-devel
BuildRequires: xcb-util-wm-devel
BuildRequires: xcb-util-xrm-devel
Requires: cairo
Requires: jsoncpp
Requires: python2
Requires: xcb-proto
Requires: xcb-util-image
Requires: xcb-util-wm
Requires: xcb-util-xrm

%description
A fast and easy-to-use tool for creating status bars.

%prep
rm -rf polybar
git clone --branch %{version} --recursive https://github.com/jaagr/polybar
cd polybar

%build
cd polybar
mkdir build
cd build
cmake .. \
    -DCMAKE_INSTALL_PREFIX:PATH=/usr \
    -DCMAKE_C_COMPILER="cc" \
    -DCMAKE_CXX_COMPILER="c++" \
    -DENABLE_ALSA:BOOL="ON" \
    -DENABLE_I3:BOOL="ON" \
    -DENABLE_MPD:BOOL="ON" \
    -DENABLE_NETWORK:BOOL="ON" \
    -DENABLE_CURL:BOOL="ON"
make -j

%install
cd polybar/build
%make_install
%check

%files
/usr/bin/polybar
/usr/bin/polybar-msg
/usr/share/doc/polybar/config
/usr/share/man/man1/polybar.1.gz
/usr/share/zsh/site-functions/_polybar
/usr/share/zsh/site-functions/_polybar_msg
/usr/share/bash-completion/completions/polybar

%changelog
