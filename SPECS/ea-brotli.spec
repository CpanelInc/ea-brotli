Name: ea-brotli
Summary: Brotli compression format
Version: 1.0.2
# Doing release_prefix this way for Release allows for OBS-proof versioning, See EA-4544 for more details
%define release_prefix 1
Release: %{release_prefix}%{?dist}.cpanel
Vendor: cPanel, Inc.
Group: System Environment/Libraries
License: LGPLv2+ and GPLv2+
URL: hhttps://github.com/google/brotli

Source: https://github.com/google/brotli/archive/v1.0.2.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Brotli is a generic-purpose lossless compression algorithm that compresses data using a combination of a
modern variant of the LZ77 algorithm, Huffman coding and 2nd order context modeling, with a compression
 ratio comparable to the best currently available general-purpose compression methods. It is similar in
 speed with deflate but offers more dense compression.

%package devel
Summary: Header files and development libraries for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
BuildRequires: cmake

%description devel
This package contains the header files and development libraries
for %{name}. If you like to develop programs using %{name}, you will need
to install %{name}-devel.


%prep
%setup -q -n brotli-%{version}

%build

./configure-cmake --prefix=/opt/cpanel/ea-brotli
make
make test

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/opt/cpanel/ea-brotli
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, -)
/opt/cpanel/ea-brotli

%files devel
%defattr (-, root, root, -)
/opt/cpanel/ea-brotli/include

%changelog
* Thu Feb 01 2018 Dan Muey <dan@cpanel.net> - 1.0.2-1
- EA-7154: Initial brotli library for EA4
