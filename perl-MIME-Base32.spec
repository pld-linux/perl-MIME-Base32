#
# Conditional build:
%bcond_without	tests		# unit tests
#
%define	pdir	MIME
%define	pnam	Base32
Summary:	MIME::Base32 - Base32 encoder/decoder
Summary(pl.UTF-8): MIME::Base32 - koder/dekoder Base32
Name:		perl-MIME-Base32
Version:	1.303
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/MIME/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0c7735fa09e74c7f2ec93d1890b8c6c0
URL:		https://metacpan.org/dist/MIME-Base32
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Encode data similar way like MIME::Base64 does.

Main purpose is to create encrypted text used as id or key entry
typed-or-submitted by user. It is upper/lowercase safe (not
sensitive).

%description -l pl.UTF-8
Ten moduł koduje dane w sposób podobny do MIME::Base64.

Głównym zastosowaniem jest tworzenie zaszyfrowanego tekstu używanego
jako identyfikator lub klucz wpisywany lub przekazywany przez
użytkownika. Jest bezpieczny ze względu na wielkość liter (nie są one
rozróżniane).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.md
%{perl_vendorlib}/MIME/Base32.pm
%{_mandir}/man3/MIME::Base32.3pm*
