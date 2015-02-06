%define module	Email-MIME-ContentType
%define upstream_version 1.017

Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	3
Summary:	Parse a MIME Content-Type Header
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Email/Email-MIME-ContentType-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:  perl(Capture::Tiny)
BuildArch:	noarch

%description
This module is responsible for parsing email content type headers according to
section 5.1 of RFC 2045. It returns a hash as above, with entries for the
discrete type, the composite type, and a hash of attributes.

%prep
%setup -q -n %{module}-%{upstream_version}

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

