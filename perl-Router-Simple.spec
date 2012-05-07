#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Router
%define		pnam	Simple
%include	/usr/lib/rpm/macros.perl
Summary:	Router::Simple - simple HTTP router
#Summary(pl.UTF-8):	
Name:		perl-Router-Simple
Version:	0.09
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Router/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f6be0b32e536c9dab654a7cf4defe633
URL:		http://search.cpan.org/dist/Router-Simple/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Accessor
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Router::Simple is a simple router class.

Its main purpose is to serve as a dispatcher for web applications.

Router::Simple can match against PSGI $env directly, which means
it's easy to use with PSGI supporting web frameworks.



# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorlib}/Router
%{perl_vendorlib}/Router/*.pm
%{perl_vendorlib}/Router/Simple
%{_mandir}/man3/*
