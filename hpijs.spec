Summary:	HP Inkjet Server
Summary(pl):	Serwer dla drukarek HP Inkjet
Name:		hpijs
Version:	0.97
Release:	1
License:	BSD (HP Products Only)
Group:		Applications/Graphics
Group(de):	Applikationen/Grafik
Group(pl):	Aplikacje/Grafika
Source0:	http://hpinkjet.sourceforge.net/%{name}%{version}.tar.gz
Patch0:		%{name}-make-flags.patch
URL:		http://hpinkjet.sourceforge.net/
BuildRequires:	libstdc++-devel
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
%setup -q -n hpijs%{version}
%patch0 -p1

%build
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
