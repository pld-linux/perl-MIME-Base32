#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	MIME
%define	pnam	Base32
Summary:	MIME::Base32 - Base32 encoder / decoder
Summary(pl.UTF-8): MIME::Base32 - Base32 koder / dekoder
Name:		perl-MIME-Base32
Version:	1.01
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/D/DA/DANPEDER/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2e0a1df2a73dcee749c225774cac52e7
URL:		http://search.cpan.org/dist/MIME-Base32/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Encode data similar way like MIME::Base64 does.

Main purpose is to create encrypted text used as id or key entry
typed-or-submitted by user. It is upper/lowercase safe (not
sensitive).

%description -l pl.UTF-8
MIME::Base32 - Base32 koder / dekoder

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
%doc README
%{perl_vendorlib}/MIME/*.pm
%{_mandir}/man3/*
