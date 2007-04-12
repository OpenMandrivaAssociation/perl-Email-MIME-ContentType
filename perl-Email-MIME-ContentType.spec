%define module	Email-MIME-ContentType
%define name	perl-%{module}
%define version 1.01.2
%define up_version 1.012
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Parse a MIME Content-Type Header
License:	GPL or Artistic
Group:		Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Email/%{module}-%{up_version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
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


