%define module	Email-MIME-ContentType
%define name	perl-%{module}
%define up_version 1.015
%define version %perl_convert_version %{up_version}
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Parse a MIME Content-Type Header
License:	GPL or Artistic
Group:		Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Email/%{module}-%{up_version}.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module is responsible for parsing email content type headers according to
section 5.1 of RFC 2045. It returns a hash as above, with entries for the
discrete type, the composite type, and a hash of attributes.

%prep
%setup -q -n %{module}-%{up_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Email
%{_mandir}/*/*


