Summary:	HP Inkjet Server
Summary(pl):	Serwer dla drukarek HP Inkjet
Name:		hpijs
Version:	1.4.1
Release:	1
License:	BSD
Group:		Applications/System
Source0:	http://dl.sourceforge.net/hpinkjet/%{name}-%{version}.tar.gz
# Source0-md5:	fff91a62e0917a5fac6111f524ed7d21
URL:		http://hpinkjet.sourceforge.net/
Patch0:		%{name}-ac_fixes.patch
Patch1:		%{name}-DESTDIR.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
# think about this...
BuildRequires:	cups-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	ghostscript <= 7.00-3

%define		_gcc_ver	%(%{__cc} -dumpversion | cut -b 1)
%if %{_gcc_ver} == 2
%define		__cxx		"%{__cc}"
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

%prep
%setup -q
%patch0 -p1
%patch1 -p1 -b .wiget

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
CXXFLAGS="%{rpmcflags} -fno-exceptions -fno-rtti"
%configure \
	--enable-foomatic-install \
	--enable-cups-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT$(cups-config --datadir)/model \
	$RPM_BUILD_ROOT$(cups-config --serverbin)/filter

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc hpijs_readme.html
%attr(755,root,root) %{_bindir}/hpijs
# move this to foomatic subpackage ?
%{_datadir}/ppd/HP
