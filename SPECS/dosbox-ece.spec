Name:           dosbox-ece
Version:        r4180
Release:        1%{?dist}
Provides:       dosbox

Summary:        x86/DOS emulator with sound and graphics

Group:          Applications/Emulators
License:        GPLv2+
URL:            https://blog.yesterplay80.net/dosbox-ece-en/
# https://dosbox.yesterplay80.net/?do=download&file=DOSBox%20ECE%20r4180%20(Linux%20source).7z
Source0:        DOSBox ECE %{version} (Linux source).7z
Source1:        dosbox.desktop
# From https://commons.wikimedia.org/wiki/File:DOSBox_icon.png
Source2:        dosbox.png
Source3:        dosbox.appdata.xml
# add translations {da,de,es,fr,it,ko,pt,ru} rhbz#752307
Source10:       DOSBox-0.74-DK.zip
Source11:       DOSBox-german-lang-0.74.zip
Source12:       DOSBox-spanish-074.zip
Source13:       DOSBox-0.74-lang-french.zip
Source14:       DOSBox-ita-lang-0.74.zip
Source15:       DOSBox-Kor-Lang-0.74.zip
Source16:       DOSBox-portuguese-br-lang-074.zip
Source17:       DOSBox-russian-lang-074.zip
Source18:       PATCHES.txt
Source19:       README-pixel-perfect.txt

BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  libpng-devel
BuildRequires:  SDL-devel
BuildRequires:  SDL_net-devel
BuildRequires:  SDL_sound-devel
BuildRequires:  desktop-file-utils
BuildRequires:  alsa-lib-devel
BuildRequires:  libGLU-devel
BuildRequires:  munt-devel
BuildRequires:  opusfile-devel
BuildRequires:  p7zip
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

Currently, DOSBox ECE differs from normal DOSBox in these features:

Emulation of a 3Dfx Vooodoo card through OpenGL (No external Glide wrapper needed!)
4x, 5x and 6x scaling in windowed mode is possible
Pixel-perfect output mode for undistorted scaling of the picture
Improved emulation of OPL3 (a FM sound synthesis chip from Yamaha)
Improved sound of PC speaker emulation
Emulation of the Roland MT-32 midi synthesizer
Integration of Fluidsynth (a software MIDI synthesizer with Soundfont support)
Support for up to 10 joystick axis and 2 D-pads (full use of two 360 compatible controllers)
Mouse buttons mappable to keyboard or controller buttons
Separate sensitivity settings for the X and Y axis of the mouse
Supports up to 384 MB of memory, required for running Windows 9x on top of DOSBox ECE
8MB video memory, reducing sprite flickering in games using the Build engine (“Duke Nukem 3D”, “Blood”, etc.)


%prep
7za x '%{SOURCE0}' || exit $?
cp '%{SOURCE18}' '%{SOURCE19}' .
./autogen.sh

%build
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

mkdir -p %{buildroot}%{_datadir}/dosbox/translations/{da,de,es,fr,it,ko,pt,ru}
pushd %{buildroot}%{_datadir}/dosbox/translations/da
unzip -j %{SOURCE10}
popd
pushd %{buildroot}%{_datadir}/dosbox/translations/de
unzip %{SOURCE11}
popd
pushd %{buildroot}%{_datadir}/dosbox/translations/es
unzip %{SOURCE12}
popd
pushd %{buildroot}%{_datadir}/dosbox/translations/fr
unzip %{SOURCE13}
popd
pushd %{buildroot}%{_datadir}/dosbox/translations/it
unzip -j %{SOURCE14}
popd
pushd %{buildroot}%{_datadir}/dosbox/translations/ko
unzip %{SOURCE15}
popd
pushd %{buildroot}%{_datadir}/dosbox/translations/pt
unzip %{SOURCE16}
popd
pushd %{buildroot}%{_datadir}/dosbox/translations/ru
unzip %{SOURCE17}
popd

%files
%doc AUTHORS ChangeLog COPYING NEWS README THANKS PATCHES.txt README-pixel-perfect.txt
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/applications/*
%{_datadir}/metainfo/*
%{_datadir}/pixmaps/dosbox.png
%{_datadir}/dosbox


%changelog
* Sun Jan 06 2019 Andrey Kuleshov <ksv0x07c2@gmail.com> - r4180-1
- Initial version based on spec file for dosbox-0.74-26
