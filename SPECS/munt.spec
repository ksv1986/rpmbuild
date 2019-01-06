Name: munt
Version: 2.3.0
Release: 1%{?dist}
Summary: MT-32, CM-32L and LAPC-I synthesiser modules emulator
Group: Sound
Url: http://munt.sourceforge.net/
License: GPL2
Packager: Andrey Kuleshov <ksv0x07c2@gmail.com>

Source0: https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires: cmake gcc-c++ glib2-devel alsa-lib-devel

%description
mt32emu
=======
mt32emu is a C/C++ library which allows to emulate (approximately) the Roland
MT-32, CM-32L and LAPC-I synthesiser modules.

mt32emu_alsadrv
===============
ALSA MIDI driver uses mt32emu to provide ALSA MIDI interface for Linux applications (now obsolete).

mt32emu_smf2wav
===============
mt32emu-smf2wav makes use of mt32emu to produce a WAVE file from an SMF file.
The output file corresponds a digital recording from a Roland MT-32, CM-32L and LAPC-I
synthesiser module.

%package devel
Group: Development/Libraries
Summary: Development files for mt32emu.
Requires: %{name}

%description devel
mt32emu development files.

%prep
%setup -n %{name}-%{version}

%build
%cmake \
	-Dmunt_WITH_MT32EMU_QT=FALSE \
	-Dlibmt32emu_SHARED=TRUE \

%make_build
%make_build -C mt32emu_alsadrv/ mt32d \
	INCLUDES="-I../mt32emu/include" \
	CXXFLAGS="-O2 -Wno-write-strings -Wno-unused-result -Wno-deprecated-declarations \
		-L../mt32emu"

%install
%make_install
mv %{buildroot}%{_docdir}/munt doc
mkdir doc/alsadrv/
cp -a mt32emu_alsadrv/*.txt doc/alsadrv/
install -m755 mt32emu_alsadrv/mt32d %{buildroot}%{_bindir}/

%files
%{_bindir}/*
%{_libdir}/*.so.*
%doc doc/*

%files devel
%{_libdir}/*.so
%{_includedir}/mt32emu

%changelog
* Sun Jan 06 2019 Andrey Kuleshov <ksv0x07c2@gmail.com> 2.3.0-1
- initial version
- only smf2wav and alsadrv are built, no QT, no GUI
