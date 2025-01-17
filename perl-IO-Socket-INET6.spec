%define modname	IO-Socket-INET6
%define modver 2.72

Summary:	Object interface for AF_INET|AF_INET6 domain sockets
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	10
License:	BSD-like
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/IO/IO-Socket-INET6-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-Socket6
BuildRequires:	perl-devel
BuildRequires:  perl-Test
BuildRequires:  perl-Test-Simple

%description
IO::Socket::INET6 provides an object interface to creating and using sockets in
both AF_INET|AF_INET6 domain. It is built upon the IO::Socket interface and
inherits all the methods defined by IO::Socket.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# itchka@compuserve.com Disable tests. Socket creation in doubt in docker
# make test

%install
%makeinstall_std

%files
%doc ChangeLog README
%{perl_vendorlib}/IO
%{_mandir}/man3/*



