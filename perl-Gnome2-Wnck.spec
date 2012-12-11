%define	upstream_name	 Gnome2-Wnck
%define	upstream_version 0.16

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Perl module for the gnome2-2.x wnck libraries
License:	GPL+ or Artistic
Group:		Development/GNOME and GTK+
Url:		http://gtk2-perl.sf.net/
Source0:	http://prdownloads.sourceforge.net/gtk2-perl/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:  libwnck-devel >= 2.19.5
BuildRequires:	perl-devel
BuildRequires:  perl-ExtUtils-Depends
BuildRequires:  perl-ExtUtils-PkgConfig 
BuildRequires:	perl-Glib => 1.00
BuildRequires:  perl-Gtk2
BuildRequires:  pkgconfig
BuildRequires:  x11-server-xvfb
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

Conflicts:	drakxtools < 9.1-15mdk
Requires:	perl-Glib >= 1.00

%description
This module provides perl access to GNOME-2.x wnck libraries.

libwnck is Window Navigator Construction Kit, i.e. a library to use
for writing pagers and taskslists and stuff.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
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
%{perl_vendorarch}/Gnome2/*
%{perl_vendorarch}/auto/Gnome2/*


%changelog
* Wed Jul 21 2010 Thierry Vignaud <tv@mandriva.org> 0.160.0-1mdv2011.0
+ Revision: 556661
- buildrequires x11-server-xvfb instead of XFree86-Xvfb

* Mon Aug 03 2009 J√©r√¥me Quelin <jquelin@mandriva.org> 0.160.0-1mdv2010.0
+ Revision: 408412
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.16-2mdv2009.0
+ Revision: 268518
- rebuild early 2009.0 package (before pixel changes)

* Mon Apr 14 2008 Thierry Vignaud <tv@mandriva.org> 0.16-1mdv2009.0
+ Revision: 192887
- new release

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.15-2mdv2008.1
+ Revision: 152096
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 11 2007 Thierry Vignaud <tv@mandriva.org> 0.15-1mdv2008.1
+ Revision: 117311
- remove patch 0 (merged)
- new release
- add download URI

* Wed Aug 22 2007 Frederic Crozat <fcrozat@mandriva.com> 0.14-3mdv2008.0
+ Revision: 68897
- Patch0 (CVS): fix support for libwnck >= 2.19.5

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild for new libwnck


* Wed Jul 26 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.13-1mdv2007.0
- new release

* Tue Feb 07 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.12-1mdk
- new release

* Thu Oct 13 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.11-1mdk
- new release

* Tue Oct 11 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 0.10-5mdk
- Fix BuildRequires

* Sat Oct 01 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 0.10-4mdk
- buildrequires fix

* Sat Oct 01 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 0.10-3mdk
- Add buildrequires

* Fri Apr 29 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.10-2mdk
- rebuild for new wnck

* Fri Feb 25 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.10-1mdk
- new release

* Wed Feb 09 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.09-2mdk
- rebuild for new perl

* Wed Nov 10 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.09-1mdk
- new release

* Sat Aug 14 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.07-1mdk
- new release

* Wed Jul 28 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.06-1mdk
- new release
- drop patch 0 (fixed upstream)

* Tue Jul 20 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.05-2mdk
- fix warnings at build time

* Tue Jul 20 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.05-1mdk
- new release
- patch 0: fix build with libwnck-2.6.x where x < 3
- fix build

* Thu Jun 03 2004 Per √òyvind Karlsen <peroyvind@linux-mandrake.com> 0.02-1mdk
- 0.02
- fix build when there's no xdisplay available
- cosmetics

* Sat Jan 10 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.01-1mdk
- initial release

