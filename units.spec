Summary: A utility for converting amounts from one unit to another
Name: units
Version: 2.01
Release: 5%{?dist}
Source: ftp://ftp.gnu.org/gnu/units/%{name}-%{version}.tar.gz
URL: http://www.gnu.org/software/units/units.html
License: GPLv3+
Group: Applications/Engineering
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info
BuildRequires: bison
BuildRequires: ncurses-devel
BuildRequires: readline-devel

# mention the --check-verbose option in units.1 man page
Patch1: 0001-units.man-mention-the-verbose-check-option.patch

%description
Units converts an amount from one unit to another, or tells you what
mathematical operation you need to perform to convert from one unit to
another. The units program can handle multiplicative scale changes as 
well as conversions such as Fahrenheit to Celsius.

%prep
%setup -q
%patch1 -p1

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT 

gzip $RPM_BUILD_ROOT%{_infodir}/units.info

# provide a man page for units_cur as a symlink to units.1
ln -s units.1 %{buildroot}%{_mandir}/man1/units_cur.1

%check
make check

%post
if [ -e %{_infodir}/units.info.gz ]; then
  /sbin/install-info %{_infodir}/units.info.gz %{_infodir}/dir || :
fi

%preun
if [ $1 = 0 -a -e %{_infodir}/units.info.gz ]; then
  /sbin/install-info --delete %{_infodir}/units.info.gz %{_infodir}/dir || :
fi

%files
%doc ChangeLog COPYING NEWS README
%{_bindir}/*
%{_datadir}/units
%{_infodir}/*
%{_mandir}/man1/*

%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 2.01-5
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.01-4
- Mass rebuild 2013-12-27

* Mon May 20 2013 Kamil Dudka <kdudka@redhat.com> - 2.01-3
- provide a man page for units_cur as a symlink to units.1
- mention the --check-verbose option in units.1 man page

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 25 2012 Kamil Dudka <kdudka@redhat.com> - 2.01-1
- new upstream release

* Fri Sep 07 2012 Kamil Dudka <kdudka@redhat.com> - 2.00-4
- run the upstream smoke-test during build

* Tue Aug 28 2012 Kamil Dudka <kdudka@redhat.com> - 2.00-3
- fix specfile issues reported by the fedora-review script

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.00-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 02 2012 Kamil Dudka <kdudka@redhat.com> - 2.00-1
- new upstream release, dropped applied patches
- patch Makefile.in to respect $(DESTDIR)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.88-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 17 2011 Kamil Dudka <kdudka@redhat.com> - 1.88-5
- improve the units-1.88-coverity.patch (thanks to Adrian Mariano)

* Wed Nov 16 2011 Kamil Dudka <kdudka@redhat.com> - 1.88-4
- fix code defects found by Coverity

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.88-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed May 05 2010 Kamil Dudka <kdudka@redhat.com> - 1.88-2
- fix typo in man page (#588565)

* Tue Feb 23 2010 Kamil Dudka <kdudka@redhat.com> - 1.88-1
- new upstream release, dropped applied patches

* Tue Dec 01 2009 Kamil Dudka <kdudka@redhat.com> - 1.87-7
- add BuildRequires for bison

* Tue Dec 01 2009 Kamil Dudka <kdudka@redhat.com> - 1.87-6
- update license to GPLv3+, sanitize specfile
- fix tons of gcc warnings

* Thu Aug 20 2009 Zdenek Prikryl <zprikryl@redhat.com> - 1.87-5
- Don't complain if installing with --excludedocs (#515941)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.87-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.87-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.87-2
- Autorebuild for GCC 4.3

* Wed Oct 31 2007 Zdenek Prikryl <zprikryl@redhat.com> - 1.87-1
- New version 1.87 

* Thu Aug 23 2007 Harald Hoyer <harald@redhat.com> - 1.86-7
- changed license tag

* Thu Jul 05 2007 Florian La Roche <laroche@redhat.com>
- fix preun script to properly remove the info file

* Fri Mar 23 2007 Harald Hoyer <harald@redhat.com> - 1.86-5
- more specfile cleanups

* Tue Mar 20 2007 Harald Hoyer <harald@redhat.com> - 1.86-4
- added readline build requirement
- changed BUILDROOT

* Wed Jan 24 2007 Harald Hoyer <harald@redhat.com> - 1.86-3
- fixed previous fix for rhbz#220533

* Tue Jan 23 2007 Florian La Roche <laroche@redhat.com> - 1.86-2
- rhbz#220533

* Mon Nov 13 2006 Florian La Roche <laroche@redhat.com> - 1.86-1
- 1.86

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.85-1.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.85-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.85-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Jul 19 2005 Harald Hoyer <harald@redhat.com> - 1.85-1
- version 1.85

* Thu Mar 03 2005 Harald Hoyer <harald@redhat.com> 
- rebuilt

* Wed Jan 12 2005 Tim Waugh <twaugh@redhat.com>
- Rebuilt for new readline.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun 24 2003 Harald Hoyer <harald@redhat.de> 1.80-8
- au is now astronomicalunit

* Wed Jun 11 2003 Harald Hoyer <harald@redhat.de> 1.80-7
- fix parsecs #96982

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri May 23 2003 Jeremy Katz <katzj@redhat.com> 1.80-5
- fix build with gcc 3.3

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Dec 17 2002 Harald Hoyer <harald@redhat.de> 1.80-2
- changed description

* Tue Nov 05 2002 Harald Hoyer <harald@redhat.de> 1.80-1
- update to version 1.80

* Tue Jul 23 2002 Harald Hoyer <harald@redhat.de>
- removed prestripping

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Dec 14 2001 Harald Hoyer <harald@redhat.de> 1.74-1
- bumped version
- this fixed #54971

* Fri May 11 2001 Bernhard Rosenkraenzer <bero@redhat.com> 1.55-10
- rebuild with new readline

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jun 11 2000 Bill Nottingham <notting@redhat.com>
- rebuild, FHS stuff

* Wed Apr  5 2000 Bill Nottingham <notting@redhat.com>
- rebuild against current ncurses/readline

* Fri Mar 24 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- rebuild with new readline

* Thu Feb  3 2000 Bill Nottingham <notting@redhat.com>
- handle compressed man pages

* Mon Nov 22 1999 Bill Nottingham <notting@redhat.com>
- fix install-info (#6631)

* Mon Sep 13 1999 Bill Nottingham <notting@redhat.com>
- strip files

* Mon Aug  2 1999 Bill Nottingham <notting@redhat.com>
- update to 1.55

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 12)

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- built package for 6.0

* Sun Aug 23 1998 Jeff Johnson <jbj@redhat.com>
- units.lib corrections (problem #685)

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 21 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
