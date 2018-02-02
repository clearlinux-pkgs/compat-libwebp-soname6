#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : compat-libwebp-soname6
Version  : 0.5.2
Release  : 3
URL      : https://github.com/webmproject/libwebp/archive/v0.5.2.tar.gz
Source0  : https://github.com/webmproject/libwebp/archive/v0.5.2.tar.gz
Summary  : Library for the WebP graphics format (decode only)
Group    : Development/Tools
License  : BSD-3-Clause
Requires: compat-libwebp-soname6-bin
Requires: compat-libwebp-soname6-lib
Requires: compat-libwebp-soname6-doc
BuildRequires : freeglut-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libjpeg-turbo-dev32
BuildRequires : libpng-dev32
BuildRequires : mesa-dev32
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : sed
BuildRequires : setuptools

%description
__   __  ____  ____  ____
/  \\/  \/  _ \/  _ )/  _ \
\       /   __/  _  \   __/
\__\__/\____/\_____/__/ ____  ___
/ _/ /    \    \ /  _ \/ _/
/  \_/   / /   \ \   __/  \__
\____/____/\_____/_____/____/v0.5.2

%package bin
Summary: bin components for the compat-libwebp-soname6 package.
Group: Binaries

%description bin
bin components for the compat-libwebp-soname6 package.


%package dev
Summary: dev components for the compat-libwebp-soname6 package.
Group: Development
Requires: compat-libwebp-soname6-lib
Requires: compat-libwebp-soname6-bin
Provides: compat-libwebp-soname6-devel

%description dev
dev components for the compat-libwebp-soname6 package.


%package dev32
Summary: dev32 components for the compat-libwebp-soname6 package.
Group: Default
Requires: compat-libwebp-soname6-lib32
Requires: compat-libwebp-soname6-bin
Requires: compat-libwebp-soname6-dev

%description dev32
dev32 components for the compat-libwebp-soname6 package.


%package doc
Summary: doc components for the compat-libwebp-soname6 package.
Group: Documentation

%description doc
doc components for the compat-libwebp-soname6 package.


%package lib
Summary: lib components for the compat-libwebp-soname6 package.
Group: Libraries

%description lib
lib components for the compat-libwebp-soname6 package.


%package lib32
Summary: lib32 components for the compat-libwebp-soname6 package.
Group: Default

%description lib32
lib32 components for the compat-libwebp-soname6 package.


%prep
%setup -q -n libwebp-0.5.2
pushd ..
cp -a libwebp-0.5.2 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1495234901
export CFLAGS="$CFLAGS -fstack-protector-strong "
export FCFLAGS="$CFLAGS -fstack-protector-strong "
export FFLAGS="$CFLAGS -fstack-protector-strong "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong "
%autogen --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%autogen --disable-static  --disable-gl --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1495234901
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/cwebp
%exclude /usr/bin/dwebp

%files dev
%defattr(-,root,root,-)
%exclude /usr/include/webp/decode.h
%exclude /usr/include/webp/encode.h
%exclude /usr/include/webp/types.h
%exclude /usr/lib64/libwebp.so
%exclude /usr/lib64/pkgconfig/libwebp.pc

%files dev32
%defattr(-,root,root,-)
%exclude /usr/lib32/libwebp.so
%exclude /usr/lib32/pkgconfig/32libwebp.pc
%exclude /usr/lib32/pkgconfig/libwebp.pc

%files doc
%defattr(-,root,root,-)
%exclude /usr/share/man/man1/cwebp.1
%exclude /usr/share/man/man1/dwebp.1

%files lib
%defattr(-,root,root,-)
/usr/lib64/libwebp.so.6
/usr/lib64/libwebp.so.6.0.2

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libwebp.so.6
/usr/lib32/libwebp.so.6.0.2
