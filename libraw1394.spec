Summary:	Interface to Linux IEEE-1394 subsystem
Summary(pl):	Biblioteka do obs³ugi podsystemu IEEE-1394
Name:		libraw1394
Version:	0.9.0
Release:	4
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libraw1394/%{name}_%{version}.tar.gz
# Source0-md5: 56fc0bc6f00efdebb635dcc52d91f7bc
Patch0:		%{name}-build.patch
Patch1:		%{name}-am18.patch
URL:		http://libraw1394.sourceforge.net/
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
Summary:	libraw1394 static library
Summary(pl):	Statyczna biblioteka do obs³ugi formatu IEEE-1394
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
libraw1394 static librawy.

%description static -l pl
Statyczna biblioteka libraw1394.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	aclocaldir=%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README NEWS
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libraw1394
%{_aclocaldir}/libraw1394.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
