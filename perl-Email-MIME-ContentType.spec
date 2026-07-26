%define module	Email-MIME-ContentType
Name:		perl-%{module}
Version:	1.028
Release:	2
Summary:	Parse a MIME Content-Type Header
License:	GPL or Artistic
Group:		Development/Perl
URL:		https://github.com/rjbs/Email-MIME-ContentType
Source:		https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Email-MIME-ContentType-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:  perl(Capture::Tiny)
BuildArch:	noarch

%description
This module is responsible for parsing email content type headers according to
section 5.1 of RFC 2045. It returns a hash as above, with entries for the
discrete type, the composite type, and a hash of attributes.

%prep
%setup -q -n %{module}-%{version}

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

