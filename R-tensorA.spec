#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-tensorA
Version  : 0.36.2
Release  : 41
URL      : https://cran.r-project.org/src/contrib/tensorA_0.36.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/tensorA_0.36.2.tar.gz
Summary  : Advanced Tensor Arithmetic with Named Indices
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: R-tensorA-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
linear algebra with tensors and computation with data sets of
        tensors on a higher level abstraction. It includes Einstein and
        Riemann summing conventions, dragging, co- and contravariate
        indices, parallel computations on sequences of tensors.

%package lib
Summary: lib components for the R-tensorA package.
Group: Libraries

%description lib
lib components for the R-tensorA package.


%prep
%setup -q -c -n tensorA
cd %{_builddir}/tensorA

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605891250

%install
export SOURCE_DATE_EPOCH=1605891250
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tensorA
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tensorA
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tensorA
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc tensorA || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/tensorA/DESCRIPTION
/usr/lib64/R/library/tensorA/INDEX
/usr/lib64/R/library/tensorA/Meta/Rd.rds
/usr/lib64/R/library/tensorA/Meta/features.rds
/usr/lib64/R/library/tensorA/Meta/hsearch.rds
/usr/lib64/R/library/tensorA/Meta/links.rds
/usr/lib64/R/library/tensorA/Meta/nsInfo.rds
/usr/lib64/R/library/tensorA/Meta/package.rds
/usr/lib64/R/library/tensorA/NAMESPACE
/usr/lib64/R/library/tensorA/R/tensorA
/usr/lib64/R/library/tensorA/R/tensorA.rdb
/usr/lib64/R/library/tensorA/R/tensorA.rdx
/usr/lib64/R/library/tensorA/help/AnIndex
/usr/lib64/R/library/tensorA/help/aliases.rds
/usr/lib64/R/library/tensorA/help/paths.rds
/usr/lib64/R/library/tensorA/help/tensorA.rdb
/usr/lib64/R/library/tensorA/help/tensorA.rdx
/usr/lib64/R/library/tensorA/html/00Index.html
/usr/lib64/R/library/tensorA/html/R.css
/usr/lib64/R/library/tensorA/tests/checker.R
/usr/lib64/R/library/tensorA/tests/examples.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/tensorA/libs/tensorA.so
/usr/lib64/R/library/tensorA/libs/tensorA.so.avx2
