Summary:	Interface to Linux IEEE-1394 subsystem
Summary(pl):	Biblioteka do obs³ugi podsystemu IEEE-1394
Name:		libraw1394
Version:	0.9.0
Release:	3
License:	LGPL
Group:		Libraries
Source0:	http://download.sourceforge.net/libraw1394/%{name}_%{version}.tar.gz
URL:		http://libraw1394.sourceforge.net
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
libraw1394 is the only supported interface to the kernel side raw1394
of the Linux IEEE-1394 subsystem, which provides direct access to the
connected 1394 buses to user space. Through libraw1394/raw1394,
applications can directly send to and receive from other nodes without
requiring a kernel driver for the protocol in question.

%description -l pl
libraw1394 jest jedynym supportowanym po stronie kernela linuksowego
raw1394 subsystemu IEEE-1394, który zapewnia bezpo¶redni dostêp do
szyn 1394 w przestrzeni u¿ytkownika. Poprzez libraw1394/raw1394
aplikacje mog± bezpo¶rednio wysy³aæ i otrzymywaæ z innych koñcówek bez
potrzeby kernelowego drivera w zapytaniu.

%package devel
Summary:	libraw1394 header files
Summary(pl):	Pliki nag³ówkowe biblioteki libraw1394
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
libraw1394 devel package.

%description devel -l pl
Pliki nag³ówkowe biblioteki libraw1394.

%package static
Summary:	libraw1394 static libraries
Summary(pl):	Statyczne biblioteki do obs³ugi formatu IEEE-1394
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
libraw1394 static package.

%description static -l pl
libraw1394 - statyczne biblioteki.

%prep
%setup  -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	aclocaldir=%{_aclocaldir}

gzip -9nf README NEWS

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,NEWS}*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/libraw1394
%{_aclocaldir}/libraw1394.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
