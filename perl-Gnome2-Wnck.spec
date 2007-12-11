%define	module	Gnome2-Wnck
%define	name	perl-%{module}
%define	version	0.14
%define	release	%mkrel 3
%define	fmodule	Gnome2/Wnck

Summary:	Perl module for the gnome2-2.x wnck libraries
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/GNOME and GTK+
Source0:	http://prdownloads.sourceforge.net/gtk2-perl/%{module}-%{version}.tar.bz2
# (fc) fix support of libwnck >= 2.19.5 (CVS)
Patch0:		Gnome2-Wnck-0.14-libwnck219.patch
URL:		http://gtk2-perl.sf.net/
BuildRequires:	perl-Glib => 1.00 perl-Gtk2 XFree86-Xvfb
BuildRequires:	perl-devel perl-ExtUtils-Depends perl-ExtUtils-PkgConfig 
BuildRequires:  pkgconfig
BuildRequires:  libwnck-devel >= 2.19.5
Requires:	perl-Glib >= 1.00
Conflicts:	drakxtools < 9.1-15mdk
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module provides perl access to GNOME-2.x wnck libraries.

libwnck is Window Navigator Construction Kit, i.e. a library to use
for writing pagers and taskslists and stuff.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1 -b .fixlibwnck219
find -type d -name CVS | rm -rf 

%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Os -s"
export GTK2_PERL_CFLAGS="$RPM_OPT_FLAGS"
perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="$RPM_OPT_FLAGS"
#%make test || :

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc LICENSE 
%{_mandir}/*/*
%{perl_vendorarch}/%fmodule
%{perl_vendorarch}/%fmodule.pm
%{perl_vendorarch}/auto/%fmodule


