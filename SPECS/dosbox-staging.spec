Name:           dosbox-staging
Version:        git
Release:        1%{?dist}
Provides:       dosbox

Summary:        x86/DOS emulator with sound and graphics

%global         commit 851b65c5f9af2ca4872e52b36b80f73786ff867d
%global         shortcommit %(c=%{commit}; echo ${c:0:7})

Group:          Applications/Emulators
License:        GPLv2+
URL:            https://github.com/dosbox-staging/dosbox-staging
Source0:        https://github.com/dosbox-staging/dosbox-staging/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:        dosbox.desktop
# From https://commons.wikimedia.org/wiki/File:DOSBox_icon.png
Source2:        dosbox.png
Source3:        dosbox.appdata.xml

BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  libpng-devel
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_net-devel
BuildRequires:  SDL2_sound-devel
BuildRequires:  desktop-file-utils
BuildRequires:  alsa-lib-devel
BuildRequires:  libGLU-devel
BuildRequires:  munt-devel
BuildRequires:  opusfile-devel
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool

Requires: hicolor-icon-theme

%description

DOSBox is a DOS-emulator using SDL for easy portability to different
platforms. DOSBox has already been ported to several different platforms,
such as Windows, BeOS, Linux, Mac OS X...
DOSBox emulates a 286/386 realmode CPU, Directory FileSystem/XMS/EMS,
a SoundBlaster card for excellent sound compatibility with older games...
You can "re-live" the good old days with the help of DOSBox, it can run plenty
of the old classics that don't run on your new computer!

dosbox-staging attempts to modernize the DOSBox codebase by using current
development practices and tools, fixing issues, and adding features that
better support today's systems.


%prep
%autosetup -n dosbox-staging-%{commit}

%build
./autogen.sh
%configure --enable-core-inline
%{__make} %{_smp_mflags}

%check
%{__make} check

%install
make install DESTDIR=%{buildroot}

desktop-file-install \
%if 0%{?fedora} && 0%{?fedora} < 19
  --vendor fedora            \
%endif
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE1}

mkdir -p %{buildroot}%{_datadir}/pixmaps
install -p -m 0644 %SOURCE2 %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/metainfo
install -p -m 0644 %SOURCE3 %{buildroot}%{_datadir}/metainfo

%files
%doc AUTHORS COPYING README.md THANKS
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/applications/*
%{_datadir}/metainfo/*
%{_datadir}/pixmaps/dosbox.png


%changelog
* Sun Jan 06 2019 Andrey Kuleshov <ksv0x07c2@gmail.com> - r4180-1
- Initial version based on spec file for dosbox-0.74-26
