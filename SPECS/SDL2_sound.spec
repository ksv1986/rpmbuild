Name:           SDL2_sound
Version:        1.9.0
Release:        1%{?dist}
Summary:        Library handling decoding of several popular sound file formats
License:        LGPLv2+
URL:            http://www.icculus.org/SDL_sound
%global hgrev   9262f9205898
# http://hg.icculus.org/icculus/SDL_sound/archive/9262f9205898.tar.gz
Source0:        SDL_sound-%{hgrev}.tar.gz
BuildRequires:  SDL2-devel flac-devel speex-devel libvorbis-devel libogg-devel
BuildRequires:  mikmod-devel libmodplug-devel physfs-devel doxygen cmake

%description
SDL_sound is a library that handles the decoding of several popular sound file 
formats, such as .WAV and .OGG.

It is meant to make the programmer's sound playback tasks simpler. The 
programmer gives SDL_sound a filename, or feeds it data directly from one of 
many sources, and then reads the decoded waveform data back at her leisure. 
If resource constraints are a concern, SDL_sound can process sound data in 
programmer-specified blocks. Alternately, SDL_sound can decode a whole sound 
file and hand back a single pointer to the whole waveform. SDL_sound can 
also handle sample rate, audio format, and channel conversion on-the-fly 
and behind-the-scenes, if the programmer desires.


%package        devel
Summary:        %{summary}
Requires:       %{name} = %{version}-%{release}
Requires:       SDL2-devel

%description    devel
%{description}

This package contains the headers and libraries for SDL2_sound development.


%prep
%setup -qn SDL_sound-%{hgrev}
sed 's|FILES SDL_sound.h DESTINATION include|FILES src/SDL_sound.h DESTINATION include/SDL2|' -i CMakeLists.txt


%build
%cmake . -DSDLSOUND_BUILD_TEST=FALSE -DSDLSOUND_BUILD_STATIC=FALSE
%make_build
doxygen Doxyfile


%install
%make_install


%files
%license LICENSE.txt
%doc docs/CHANGELOG.txt docs/CREDITS.txt docs/README.txt docs/TODO.txt
%{_libdir}/libSDL2_sound.so.*


%files devel
%doc docs/html
%{_libdir}/libSDL2_sound.so
%{_includedir}/SDL2/SDL_sound.h


%changelog
* Sun Jun 30 2019 Andrey Kuleshov <ksv0x07c2@gmail.com>
- Initial RPM release.
