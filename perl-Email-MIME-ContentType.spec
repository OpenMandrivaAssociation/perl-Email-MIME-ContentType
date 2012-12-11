%define module	Email-MIME-ContentType
%define up_version 1.015

Name:		perl-%{module}
Version:	%perl_convert_version %{up_version}
Release:	2
Summary:	Parse a MIME Content-Type Header
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Email/%{module}-%{up_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module is responsible for parsing email content type headers according to
section 5.1 of RFC 2045. It returns a hash as above, with entries for the
discrete type, the composite type, and a hash of attributes.

%prep
%setup -q -n %{module}-%{up_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Email
%{_mandir}/*/*

%changelog
* Wed Feb 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.15.0-1mdv2010.0
+ Revision: 337648
- new release
- use standardized version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.01.4-3mdv2009.0
+ Revision: 256772
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 1.01.4-1mdv2008.1
+ Revision: 135833
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Jul 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.01.4-1mdv2008.0
+ Revision: 48064
- update to new version 1.014


* Tue Nov 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.01.2-1mdv2007.0
+ Revision: 87875
- new version

* Fri Nov 17 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.01.1-3mdv2007.1
+ Revision: 85092
- new version
- Import perl-Email-MIME-ContentType

* Fri Sep 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-3mdv2007.0
- Rebuild

* Mon Mar 06 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-2mdk
- fix description lines length

* Mon Mar 06 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-1mdk
- first mdk release

