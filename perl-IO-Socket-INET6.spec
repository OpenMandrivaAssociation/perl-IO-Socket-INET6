%define upstream_name IO-Socket-INET6
%define upstream_version 2.69

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Object interface for AF_INET|AF_INET6 domain sockets
License:	BSD-like
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/IO/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-Socket6
BuildRequires:	perl-devel
BuildArch:	noarch

%description
IO::Socket::INET6 provides an object interface to creating and using sockets in
both AF_INET|AF_INET6 domain. It is built upon the IO::Socket interface and
inherits all the methods defined by IO::Socket.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc ChangeLog README
%{perl_vendorlib}/IO
%{_mandir}/man3/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.670.0-4mdv2012.0
+ Revision: 765371
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 2.670.0-3
+ Revision: 763873
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.670.0-2
+ Revision: 667209
- mass rebuild

* Mon Jan 31 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.670.0-1
+ Revision: 634483
- update to new version 2.67

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 2.650.0-2mdv2011.0
+ Revision: 564735
- rebuild for perl 5.12.1

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 2.650.0-1mdv2011.0
+ Revision: 552325
- update to 2.65

* Fri Mar 26 2010 Jérôme Quelin <jquelin@mandriva.org> 2.610.0-1mdv2010.1
+ Revision: 527735
- update to 2.61

* Mon Mar 22 2010 Jérôme Quelin <jquelin@mandriva.org> 2.590.0-1mdv2010.1
+ Revision: 526447
- update to 2.59

* Tue Nov 24 2009 Jérôme Quelin <jquelin@mandriva.org> 2.570.0-1mdv2010.1
+ Revision: 469441
- update to 2.57

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 2.560.0-1mdv2010.0
+ Revision: 402558
- update to 0.56

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.56-1mdv2009.1
+ Revision: 292187
- update to new version 2.56

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 2.54-2mdv2009.0
+ Revision: 223797
- rebuild

* Mon Feb 25 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.54-1mdv2008.1
+ Revision: 174667
- update to new version 2.54
- update to new version 2.54

* Fri Feb 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.53-1mdv2008.1
+ Revision: 173869
- update to new version 2.53

* Wed Feb 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.52-1mdv2008.1
+ Revision: 162987
- new version
  drop patch, merged upstream

* Thu Jan 17 2008 Oden Eriksson <oeriksson@mandriva.com> 2.51-2mdv2008.1
+ Revision: 154096
- fix #36889 (IO-Socket-INET6 emits many warnings):
  - Added the patch with the fixes to the export / import symbols warnings
    and the testing (Shlomi Fish).
  - Restored the "percent-check" phase with "make test" (Shlomi Fish).

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Jul 29 2006 Oden Eriksson <oeriksson@mandrakesoft.com> 2.51-1mdk
- initial mandrake package

