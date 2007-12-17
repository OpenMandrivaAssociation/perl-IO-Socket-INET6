%define module	IO-Socket-INET6

Summary:	Object interface for AF_INET|AF_INET6 domain sockets
Name:		perl-%{module}
Version:	2.51
Release:	%mkrel 1
License:	BSD-like
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	http://search.cpan.org/CPAN/authors/id/M/MO/MONDEJAR/%{module}-%{version}.tar.bz2
BuildRequires:	perl-Socket6
BuildRequires:	perl-devel
BuildArch:	noarch
Provides:	perl-INET6
Obsoletes:	perl-INET6

%description
IO::Socket::INET6 provides an object interface to creating and using sockets in
both AF_INET|AF_INET6 domain. It is built upon the IO::Socket interface and
inherits all the methods defined by IO::Socket.

%prep

%setup -q -n %{module}-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

# make test hangs at "t/io_sock6..........ok 11/20"
# maybe it works as root?
#make test

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%clean 
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README
%{perl_vendorlib}/IO/Socket/INET6.pm
%{_mandir}/man3/*

