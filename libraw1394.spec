Summary:	Interface to Linux IEEE-1394 subsystem
Summary(pl.UTF-8):	Biblioteka do obsługi podsystemu IEEE-1394
Name:		libraw1394
Version:	2.1.0
Release:	2
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://ftp.kernel.org/pub/linux/libs/ieee1394/%{name}-%{version}.tar.xz
# Source0-md5:	e43a3fba606a03fec1682fbff31e53f6
URL:		http://ieee1394.wiki.kernel.org/
#URL:		http://sourceforge.net/projects/libraw1394/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	docbook-utils
BuildRequires:	libtool
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libraw1394 is the only supported interface to the kernel side raw1394
of the Linux IEEE-1394 subsystem, which provides direct access to the
connected 1394 buses to user space. Through libraw1394/raw1394,
applications can directly send to and receive from other nodes without
requiring a kernel driver for the protocol in question.

%description -l pl.UTF-8
libraw1394 jest jedynym supportowanym po stronie kernela linuksowego
raw1394 subsystemu IEEE-1394, który zapewnia bezpośredni dostęp do
szyn 1394 w przestrzeni użytkownika. Poprzez libraw1394/raw1394
aplikacje mogą bezpośrednio wysyłać i otrzymywać z innych końcówek bez
potrzeby kernelowego drivera w zapytaniu.

%package devel
Summary:	libraw1394 header files
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libraw1394
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
libraw1394 devel package.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libraw1394.

%package static
Summary:	libraw1394 static library
Summary(pl.UTF-8):	Statyczna biblioteka do obsługi formatu IEEE-1394
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
libraw1394 static librawy.

%description static -l pl.UTF-8
Statyczna biblioteka libraw1394.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}

%{__make} -C doc htmldoc

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/dumpiso
%attr(755,root,root) %{_bindir}/sendiso
%attr(755,root,root) %{_bindir}/testlibraw
%attr(755,root,root) %{_libdir}/libraw1394.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libraw1394.so.11
%{_mandir}/man1/dumpiso.1*
%{_mandir}/man1/sendiso.1*
%{_mandir}/man1/testlibraw.1*
%{_mandir}/man5/isodump.5*

%files devel
%defattr(644,root,root,755)
%doc doc/libraw1394/*
%attr(755,root,root) %{_libdir}/libraw1394.so
%{_libdir}/libraw1394.la
%{_includedir}/libraw1394
%{_pkgconfigdir}/libraw1394.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libraw1394.a
