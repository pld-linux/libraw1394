Summary:	Interface to Linux IEEE-1394 subsystem
Summary(pl):	Biblioteka do obs³ugi podsystemu IEEE-1394
Name:		libraw1394
Version:	0.8.2
Release:	1
License:	LGPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(pl):	Biblioteki
Source0:	http://download.sourceforge.net/libraw1394/%{name}_%{version}.tar.gz
URL:		http://libraw1394.sourceforge.net
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libraw1394 is the only supported interface to the kernel side raw1394 of
the Linux IEEE-1394 subsystem, which provides direct access to the
connected 1394 buses to user space.  Through libraw1394/raw1394,
applications can directly send to and receive from other nodes without
requiring a kernel driver for the protocol in question.


%package devel
Summary:	libraw1394 header files
Summary(pl):	Pliki nag³ówkowe biblioteki libraw1394
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel

%package static
Summary:	libraw1394 static libraries
Summary(pl):	Statyczne biblioteki do obs³ugi formatu IEEE-1394
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}


%description static

%prep
%setup  -q

%build
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README NEWS 

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,NEWS}*
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/libraw1394

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
