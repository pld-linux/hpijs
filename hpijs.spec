#
# Conditional build:
%bcond_without  cups	# without CUPS support
#
Summary:	HP Inkjet Server
Summary(pl):	Serwer dla drukarek HP Inkjet
Name:		hpijs
Version:	1.6.1
Release:	3
License:	BSD
Group:		Applications/System
Source0:	http://dl.sourceforge.net/hpinkjet/%{name}-%{version}.tar.gz
# Source0-md5:	03563d737f03ff94432423ad885db763
URL:		http://hpinkjet.sourceforge.net/
Patch0:		%{name}-ac_fixes.patch
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_cups:BuildRequires:	cups-devel}
BuildRequires:	libstdc++-devel
Conflicts:	ghostscript <= 7.00-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%if %{with cups}
%define 	_cupsdir 	%(cups-config --datadir)
%define		_cupsppddir	%{_cupsdir}/model
%endif

%description
The Hewlett-Packard Inkjet Server is a raster-to-pcl server or
coprocess based on the Hewlett Packard Appliance Printing Development
Kit at http://hpapdk.com/. The server is used with Ghostscript as
deskjet printer driver.

%description -l pl
Serwer Hewlett-Packard Inkjet jest serwerem raster-do-pcl lub jako
koproces bazowany na Hewlett Packard Appliance Printing Development
Kit z http://hpapdk.com/. Serwer jest u�ywany wraz z Ghostscript'em
jako sterownik dla drukarek atramentowych DeskJet.

%package ppd
Summary:	PPD database for Hewlett Packard printers
Summary(pl):	Baza danych PPD dla drukarek Hewlett Packard
Group:		Applications/System
Requires:	cups
Obsoletes:	hpijs-foomatic

%description ppd
PPD database for Hewlett Packard printers.

%description ppd -l pl
Baza danych PPD dla drukarek Hewlett Packard.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
CXXFLAGS="%{rpmcflags} -fno-exceptions -fno-rtti"
%configure \
	--enable-foomatic-install \
	%{!?with_cups:--disable-cups-install}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%if %{with cups}
install -d $RPM_BUILD_ROOT$(cups-config --datadir)/model \
	$RPM_BUILD_ROOT$(cups-config --serverbin)/filter
%endif

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with cups}
rm -f $RPM_BUILD_ROOT%{_cupsppddir}/foomatic-ppds
mv $RPM_BUILD_ROOT{%{_datadir}/ppd/HP/*,%{_cupsppddir}}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc hpijs_readme.html
%attr(755,root,root) %{_bindir}/hpijs

%if %{with cups}
%files ppd
%defattr(644,root,root,755)
%{_cupsppddir}/*
%endif
