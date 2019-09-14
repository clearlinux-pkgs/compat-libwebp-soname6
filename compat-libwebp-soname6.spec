#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : compat-libwebp-soname6
Version  : 0.5.2
Release  : 8
URL      : https://github.com/webmproject/libwebp/archive/v0.5.2.tar.gz
Source0  : https://github.com/webmproject/libwebp/archive/v0.5.2.tar.gz
Summary  : Library for the WebP graphics format (decode only)
Group    : Development/Tools
License  : BSD-3-Clause
Requires: compat-libwebp-soname6-lib = %{version}-%{release}
Requires: compat-libwebp-soname6-license = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-golang
BuildRequires : freeglut-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libjpeg-turbo-dev32
BuildRequires : libpng-dev32
BuildRequires : mesa-dev32
BuildRequires : sed
BuildRequires : tiff-dev
# Suppress generation of debuginfo
%global debug_package %{nil}

%description
__   __  ____  ____  ____
/  \\/  \/  _ \/  _ )/  _ \
\       /   __/  _  \   __/
\__\__/\____/\_____/__/ ____  ___
/ _/ /    \    \ /  _ \/ _/
/  \_/   / /   \ \   __/  \__
\____/____/\_____/_____/____/v0.5.2

%package lib
Summary: lib components for the compat-libwebp-soname6 package.
Group: Libraries
Requires: compat-libwebp-soname6-license = %{version}-%{release}

%description lib
lib components for the compat-libwebp-soname6 package.


%package lib32
Summary: lib32 components for the compat-libwebp-soname6 package.
Group: Default
Requires: compat-libwebp-soname6-license = %{version}-%{release}

%description lib32
lib32 components for the compat-libwebp-soname6 package.


%package license
Summary: license components for the compat-libwebp-soname6 package.
Group: Default

%description license
license components for the compat-libwebp-soname6 package.


%prep
%setup -q -n libwebp-0.5.2
pushd ..
cp -a libwebp-0.5.2 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1567814358
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
%autogen --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%autogen --disable-static  --disable-gl --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check
cd ../build32;
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1567814358
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/compat-libwebp-soname6
cp COPYING %{buildroot}/usr/share/package-licenses/compat-libwebp-soname6/COPYING
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
## Remove excluded files
rm -f %{buildroot}/usr/bin/cwebp
rm -f %{buildroot}/usr/bin/dwebp
rm -f %{buildroot}/usr/lib/debug
rm -f %{buildroot}/usr/lib/debug/.build-id
rm -f %{buildroot}/usr/lib/debug/.build-id/5f
rm -f %{buildroot}/usr/lib/debug/.build-id/5f/a5a9ab1099afd356c4a36c2562603978e00eaf
rm -f %{buildroot}/usr/lib/debug/.build-id/5f/a5a9ab1099afd356c4a36c2562603978e00eaf.debug
rm -f %{buildroot}/usr/lib/debug/.build-id/8d
rm -f %{buildroot}/usr/lib/debug/.build-id/8d/63d1e97fa06a419ee36b0b3ead2335a51ad340
rm -f %{buildroot}/usr/lib/debug/.build-id/8d/63d1e97fa06a419ee36b0b3ead2335a51ad340.debug
rm -f %{buildroot}/usr/lib/debug/.build-id/b9
rm -f %{buildroot}/usr/lib/debug/.build-id/b9/c47f1e69e2c6d2c2bd0d4fb13b7dd1a5237180
rm -f %{buildroot}/usr/lib/debug/.build-id/b9/c47f1e69e2c6d2c2bd0d4fb13b7dd1a5237180.debug
rm -f %{buildroot}/usr/lib/debug/.build-id/d6
rm -f %{buildroot}/usr/lib/debug/.build-id/d6/642fc7397bf8846a8139e3a33d4a50b5ee3d9c
rm -f %{buildroot}/usr/lib/debug/.build-id/d6/642fc7397bf8846a8139e3a33d4a50b5ee3d9c.debug
rm -f %{buildroot}/usr/lib/debug/usr
rm -f %{buildroot}/usr/lib/debug/usr/bin
rm -f %{buildroot}/usr/lib/debug/usr/bin/cwebp.debug
rm -f %{buildroot}/usr/lib/debug/usr/bin/dwebp.debug
rm -f %{buildroot}/usr/lib/debug/usr/lib32
rm -f %{buildroot}/usr/lib/debug/usr/lib32/libwebp.so.6.0.2.debug
rm -f %{buildroot}/usr/lib/debug/usr/lib32/libwebp.so.6.debug
rm -f %{buildroot}/usr/lib/debug/usr/lib32/libwebp.so.debug
rm -f %{buildroot}/usr/lib/debug/usr/lib64
rm -f %{buildroot}/usr/lib/debug/usr/lib64/libwebp.so.6.0.2.debug
rm -f %{buildroot}/usr/lib/debug/usr/lib64/libwebp.so.6.debug
rm -f %{buildroot}/usr/lib/debug/usr/lib64/libwebp.so.debug
rm -f %{buildroot}/usr/src/debug/build32
rm -f %{buildroot}/usr/src/debug/build32/src
rm -f %{buildroot}/usr/src/debug/build32/src/dec
rm -f %{buildroot}/usr/src/debug/build32/src/dec/alpha.c
rm -f %{buildroot}/usr/src/debug/build32/src/dec/alphai.h
rm -f %{buildroot}/usr/src/debug/build32/src/dec/buffer.c
rm -f %{buildroot}/usr/src/debug/build32/src/dec/common.h
rm -f %{buildroot}/usr/src/debug/build32/src/dec/decode_vp8.h
rm -f %{buildroot}/usr/src/debug/build32/src/dec/frame.c
rm -f %{buildroot}/usr/src/debug/build32/src/dec/idec.c
rm -f %{buildroot}/usr/src/debug/build32/src/dec/io.c
rm -f %{buildroot}/usr/src/debug/build32/src/dec/quant.c
rm -f %{buildroot}/usr/src/debug/build32/src/dec/tree.c
rm -f %{buildroot}/usr/src/debug/build32/src/dec/vp8.c
rm -f %{buildroot}/usr/src/debug/build32/src/dec/vp8i.h
rm -f %{buildroot}/usr/src/debug/build32/src/dec/vp8l.c
rm -f %{buildroot}/usr/src/debug/build32/src/dec/vp8li.h
rm -f %{buildroot}/usr/src/debug/build32/src/dec/webp.c
rm -f %{buildroot}/usr/src/debug/build32/src/dec/webpi.h
rm -f %{buildroot}/usr/src/debug/build32/src/dsp
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/alpha_processing.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/alpha_processing_mips_dsp_r2.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/alpha_processing_sse2.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/alpha_processing_sse41.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/argb.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/argb_mips_dsp_r2.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/argb_sse2.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/common_sse2.h
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/cost.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/cost_mips32.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/cost_mips_dsp_r2.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/cost_sse2.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/cpu.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/dec.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/dec_clip_tables.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/dec_mips32.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/dec_mips_dsp_r2.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/dec_msa.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/dec_neon.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/dec_sse2.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/dec_sse41.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/dsp.h
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/enc.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/enc_avx2.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/enc_mips32.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/enc_mips_dsp_r2.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/enc_neon.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/enc_sse2.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/enc_sse41.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/filters.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/filters_mips_dsp_r2.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/filters_sse2.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/lossless.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/lossless.h
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/lossless_enc.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/lossless_enc_mips32.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/lossless_enc_mips_dsp_r2.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/lossless_enc_neon.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/lossless_enc_sse2.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/lossless_enc_sse41.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/lossless_mips_dsp_r2.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/lossless_neon.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/lossless_sse2.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/rescaler.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/rescaler_mips32.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/rescaler_mips_dsp_r2.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/rescaler_neon.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/rescaler_sse2.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/upsampling.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/upsampling_mips_dsp_r2.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/upsampling_neon.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/upsampling_sse2.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/yuv.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/yuv.h
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/yuv_mips32.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/yuv_mips_dsp_r2.c
rm -f %{buildroot}/usr/src/debug/build32/src/dsp/yuv_sse2.c
rm -f %{buildroot}/usr/src/debug/build32/src/enc
rm -f %{buildroot}/usr/src/debug/build32/src/enc/alpha.c
rm -f %{buildroot}/usr/src/debug/build32/src/enc/analysis.c
rm -f %{buildroot}/usr/src/debug/build32/src/enc/backward_references.c
rm -f %{buildroot}/usr/src/debug/build32/src/enc/backward_references.h
rm -f %{buildroot}/usr/src/debug/build32/src/enc/config.c
rm -f %{buildroot}/usr/src/debug/build32/src/enc/cost.c
rm -f %{buildroot}/usr/src/debug/build32/src/enc/cost.h
rm -f %{buildroot}/usr/src/debug/build32/src/enc/delta_palettization.c
rm -f %{buildroot}/usr/src/debug/build32/src/enc/filter.c
rm -f %{buildroot}/usr/src/debug/build32/src/enc/frame.c
rm -f %{buildroot}/usr/src/debug/build32/src/enc/histogram.c
rm -f %{buildroot}/usr/src/debug/build32/src/enc/histogram.h
rm -f %{buildroot}/usr/src/debug/build32/src/enc/iterator.c
rm -f %{buildroot}/usr/src/debug/build32/src/enc/near_lossless.c
rm -f %{buildroot}/usr/src/debug/build32/src/enc/picture.c
rm -f %{buildroot}/usr/src/debug/build32/src/enc/picture_csp.c
rm -f %{buildroot}/usr/src/debug/build32/src/enc/picture_psnr.c
rm -f %{buildroot}/usr/src/debug/build32/src/enc/picture_rescale.c
rm -f %{buildroot}/usr/src/debug/build32/src/enc/picture_tools.c
rm -f %{buildroot}/usr/src/debug/build32/src/enc/quant.c
rm -f %{buildroot}/usr/src/debug/build32/src/enc/syntax.c
rm -f %{buildroot}/usr/src/debug/build32/src/enc/token.c
rm -f %{buildroot}/usr/src/debug/build32/src/enc/tree.c
rm -f %{buildroot}/usr/src/debug/build32/src/enc/vp8enci.h
rm -f %{buildroot}/usr/src/debug/build32/src/enc/vp8l.c
rm -f %{buildroot}/usr/src/debug/build32/src/enc/vp8li.h
rm -f %{buildroot}/usr/src/debug/build32/src/enc/webpenc.c
rm -f %{buildroot}/usr/src/debug/build32/src/utils
rm -f %{buildroot}/usr/src/debug/build32/src/utils/bit_reader.c
rm -f %{buildroot}/usr/src/debug/build32/src/utils/bit_reader.h
rm -f %{buildroot}/usr/src/debug/build32/src/utils/bit_reader_inl.h
rm -f %{buildroot}/usr/src/debug/build32/src/utils/bit_writer.c
rm -f %{buildroot}/usr/src/debug/build32/src/utils/bit_writer.h
rm -f %{buildroot}/usr/src/debug/build32/src/utils/color_cache.c
rm -f %{buildroot}/usr/src/debug/build32/src/utils/color_cache.h
rm -f %{buildroot}/usr/src/debug/build32/src/utils/endian_inl.h
rm -f %{buildroot}/usr/src/debug/build32/src/utils/filters.c
rm -f %{buildroot}/usr/src/debug/build32/src/utils/filters.h
rm -f %{buildroot}/usr/src/debug/build32/src/utils/huffman.c
rm -f %{buildroot}/usr/src/debug/build32/src/utils/huffman.h
rm -f %{buildroot}/usr/src/debug/build32/src/utils/huffman_encode.c
rm -f %{buildroot}/usr/src/debug/build32/src/utils/huffman_encode.h
rm -f %{buildroot}/usr/src/debug/build32/src/utils/quant_levels.c
rm -f %{buildroot}/usr/src/debug/build32/src/utils/quant_levels.h
rm -f %{buildroot}/usr/src/debug/build32/src/utils/quant_levels_dec.c
rm -f %{buildroot}/usr/src/debug/build32/src/utils/quant_levels_dec.h
rm -f %{buildroot}/usr/src/debug/build32/src/utils/random.c
rm -f %{buildroot}/usr/src/debug/build32/src/utils/random.h
rm -f %{buildroot}/usr/src/debug/build32/src/utils/rescaler.c
rm -f %{buildroot}/usr/src/debug/build32/src/utils/rescaler.h
rm -f %{buildroot}/usr/src/debug/build32/src/utils/thread.c
rm -f %{buildroot}/usr/src/debug/build32/src/utils/thread.h
rm -f %{buildroot}/usr/src/debug/build32/src/utils/utils.c
rm -f %{buildroot}/usr/src/debug/build32/src/utils/utils.h
rm -f %{buildroot}/usr/src/debug/build32/src/webp
rm -f %{buildroot}/usr/src/debug/build32/src/webp/decode.h
rm -f %{buildroot}/usr/src/debug/build32/src/webp/encode.h
rm -f %{buildroot}/usr/src/debug/build32/src/webp/format_constants.h
rm -f %{buildroot}/usr/src/debug/build32/src/webp/mux_types.h
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/examples
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/examples/cwebp.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/examples/dwebp.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/examples/example_util.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/examples/example_util.h
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/examples/image_dec.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/examples/image_dec.h
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/examples/jpegdec.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/examples/metadata.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/examples/metadata.h
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/examples/pngdec.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/examples/stopwatch.h
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/examples/tiffdec.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/examples/webpdec.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dec
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dec/alpha.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dec/alphai.h
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dec/buffer.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dec/common.h
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dec/decode_vp8.h
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dec/frame.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dec/idec.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dec/io.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dec/quant.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dec/tree.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dec/vp8.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dec/vp8i.h
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dec/vp8l.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dec/vp8li.h
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dec/webp.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dec/webpi.h
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/alpha_processing.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/alpha_processing_mips_dsp_r2.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/alpha_processing_sse2.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/alpha_processing_sse41.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/argb.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/argb_mips_dsp_r2.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/argb_sse2.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/common_sse2.h
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/cost.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/cost_mips32.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/cost_mips_dsp_r2.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/cost_sse2.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/cpu.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/dec.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/dec_clip_tables.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/dec_mips32.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/dec_mips_dsp_r2.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/dec_msa.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/dec_neon.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/dec_sse2.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/dec_sse41.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/dsp.h
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/enc.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/enc_avx2.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/enc_mips32.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/enc_mips_dsp_r2.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/enc_neon.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/enc_sse2.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/enc_sse41.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/filters.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/filters_mips_dsp_r2.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/filters_sse2.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/lossless.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/lossless.h
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/lossless_enc.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/lossless_enc_mips32.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/lossless_enc_mips_dsp_r2.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/lossless_enc_neon.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/lossless_enc_sse2.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/lossless_enc_sse41.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/lossless_mips_dsp_r2.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/lossless_neon.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/lossless_sse2.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/rescaler.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/rescaler_mips32.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/rescaler_mips_dsp_r2.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/rescaler_neon.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/rescaler_sse2.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/upsampling.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/upsampling_mips_dsp_r2.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/upsampling_neon.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/upsampling_sse2.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/yuv.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/yuv.h
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/yuv_mips32.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/yuv_mips_dsp_r2.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/dsp/yuv_sse2.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/enc
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/enc/alpha.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/enc/analysis.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/enc/backward_references.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/enc/backward_references.h
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/enc/config.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/enc/cost.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/enc/cost.h
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/enc/delta_palettization.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/enc/filter.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/enc/frame.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/enc/histogram.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/enc/histogram.h
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/enc/iterator.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/enc/near_lossless.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/enc/picture.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/enc/picture_csp.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/enc/picture_psnr.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/enc/picture_rescale.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/enc/picture_tools.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/enc/quant.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/enc/syntax.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/enc/token.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/enc/tree.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/enc/vp8enci.h
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/enc/vp8l.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/enc/vp8li.h
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/enc/webpenc.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/utils
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/utils/bit_reader.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/utils/bit_reader.h
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/utils/bit_reader_inl.h
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/utils/bit_writer.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/utils/bit_writer.h
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/utils/color_cache.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/utils/color_cache.h
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/utils/endian_inl.h
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/utils/filters.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/utils/filters.h
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/utils/huffman.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/utils/huffman.h
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/utils/huffman_encode.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/utils/huffman_encode.h
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/utils/quant_levels.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/utils/quant_levels.h
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/utils/quant_levels_dec.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/utils/quant_levels_dec.h
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/utils/random.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/utils/random.h
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/utils/rescaler.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/utils/rescaler.h
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/utils/thread.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/utils/thread.h
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/utils/utils.c
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/utils/utils.h
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/webp
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/webp/decode.h
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/webp/encode.h
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/webp/format_constants.h
rm -f %{buildroot}/usr/src/debug/libwebp-0.5.2/src/webp/mux_types.h
rm -f %{buildroot}/usr/include/webp/decode.h
rm -f %{buildroot}/usr/include/webp/encode.h
rm -f %{buildroot}/usr/include/webp/types.h
rm -f %{buildroot}/usr/lib64/libwebp.so
rm -f %{buildroot}/usr/lib64/pkgconfig/libwebp.pc
rm -f %{buildroot}/usr/lib32/libwebp.so
rm -f %{buildroot}/usr/lib32/pkgconfig/32libwebp.pc
rm -f %{buildroot}/usr/lib32/pkgconfig/libwebp.pc
rm -f %{buildroot}/usr/share/man/man1/cwebp.1
rm -f %{buildroot}/usr/share/man/man1/dwebp.1

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/libwebp.so.6
/usr/lib64/libwebp.so.6.0.2

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libwebp.so.6
/usr/lib32/libwebp.so.6.0.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/compat-libwebp-soname6/COPYING
