Summary:	HP Inkjet Server
Name:		hpijs
Version:	0.97
Release:	1
License:	BSD (HP Products Only)
Group:		Applications/Graphics
Group(de):	Applikationen/Grafik
Group(pl):	Aplikacje/Grafika
Source0:	http://hpinkjet.sourceforge.net/%{name}%{version}.tar.gz
URL:		http://hpinkjet.sourceforge.net/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	ghostscript <= 7.00-3 

%define         _prefix		/usr
%define		_bindir		%{_prefix}/bin
%define		_docdir		%{_prefix}/share/doc

%description
The Hewlett-Packard Inkjet Server is a raster-to-pcl server or
coprocess based on the Hewlett Packard Appliance Printing Development
Kit at http://hpapdk.com. The server is used with Ghostscript as
deskjet printer driver.

%prep
%setup -q -n hpijs%{version}

%build
%{__make}

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
