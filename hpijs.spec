Summary:	HP Inkjet Server
Summary(pl):	Serwer dla drukarek HP Inkjet
Name:		hpijs
Version:	1.0.2
Release:	1
License:	BSD
Group:		Applications/Graphics
Group(de):	Applikationen/Grafik
Group(pl):	Aplikacje/Grafika
Source0:	http://prdownloads.sourceforge.net/hpinkjet/%{name}-%{version}.tar.gz
URL:		http://hpinkjet.sourceforge.net/
BuildRequires:	libstdc++-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	ghostscript <= 7.00-3 

%define         _prefix		/usr
%define		_bindir		%{_prefix}/bin

%description
The Hewlett-Packard Inkjet Server is a raster-to-pcl server or
coprocess based on the Hewlett Packard Appliance Printing Development
Kit at http://hpapdk.com. The server is used with Ghostscript as
deskjet printer driver.

%description -l pl
Serwer Hewlett-Packard Inkjet jest serwerem raster-do-pcl lub jako
koproces bazowany na Hewlett Packard Appliance Printing Development
Kit z http://hpapdk.com. Serwer jest u¿ywany wraz z Ghostscript'em
jako sterownik dla drukarek atramentowych DeskJet.

%prep
%setup -q -n hpijs-%{version}

%build
rm -f missing
libtoolize --copy --force
aclocal
automake -a -c
autoconf
%configure
%{__make} BUILD_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install hpijs $RPM_BUILD_ROOT%{_bindir}

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc hpijs_readme.html printtool*.jpg printerdb_append gs_apdk.jpg
%attr(755,root,root) %{_bindir}/hpijs
