#
# Conditional build:
# _without_cups		- without CUPS support
#
Summary:	HP Inkjet Server
Summary(pl):	Serwer dla drukarek HP Inkjet
Name:		hpijs
Version:	1.5
Release:	1
License:	BSD
Group:		Applications/System
Source0:	http://dl.sourceforge.net/hpinkjet/%{name}-%{version}.tar.gz
# Source0-md5:	348bbc20f42b9d7dae4b08590649098b
URL:		http://hpinkjet.sourceforge.net/
#Patch0:		%{name}-ac_fixes.patch
#Patch1:		%{name}-DESTDIR.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
%{!?_without_cups:BuildRequires:	cups-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	ghostscript <= 7.00-3

%define		_gcc_ver	%(%{__cc} -dumpversion | cut -b 1)
%if %{_gcc_ver} == 2
%define		__cxx		"%{__cc}"
%endif

%if 0%{!?_without_cups:1}
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
Kit z http://hpapdk.com/. Serwer jest u¿ywany wraz z Ghostscript'em
jako sterownik dla drukarek atramentowych DeskJet.

%package ppd
Summary:	PPD database for Hewlett Packard printers
Summary(pl):	Baza danych PPD dla drukarek Hewlett Packard
Group:		Applications/System
# to be changed, what owns that dir???
Obsoletes:	hpijs-foomatic
Requires:	cups

%description ppd
PPD database for Hewlett Packard printers.

%description ppd -l pl
Baza danych PPD dla drukarek Hewlett Packard.

%prep
%setup -q
#%%patch0 -p1
#%%patch1 -p1 -b .wiget

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
CXXFLAGS="%{rpmcflags} -fno-exceptions -fno-rtti"
%configure \
	--enable-foomatic-install \
	%{?_without_cups:--disable-cups-install}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%if 0%{!?_without_cups:1}
install -d $RPM_BUILD_ROOT$(cups-config --datadir)/model \
	$RPM_BUILD_ROOT$(cups-config --serverbin)/filter

%endif

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%if 0%{!?_without_cups:1}
rm -f $RPM_BUILD_ROOT%{_cupsppddir}/foomatic-ppds
mv $RPM_BUILD_ROOT{%{_datadir}/ppd/HP/*,%{_cupsppddir}}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc hpijs_readme.html
%attr(755,root,root) %{_bindir}/hpijs

%if 0%{!?_without_cups:1}
%files ppd
%defattr(644,root,root,755)
%{_cupsppddir}/*
%endif
