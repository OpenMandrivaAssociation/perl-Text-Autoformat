%define module	Text-Autoformat
%define version	1.13
%define release	%mkrel 4

Name:		perl-%{module}
Version:	%{version}
Release:	%{release}
Summary:	%{module} module for perl
License:	Artistic
Group:		Text tools
URL:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/%{module}-%{version}.tar.bz2
Source1:	dot-vimrc.bz2
Source2:	dot-emacs.bz2
BuildRequires:	perl-devel perl-Text-Reform
Requires:       perl-Text-Reform
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildArch:	noarch

%description
Text::Autoformat  provides  intelligent  formatting   of   plaintext
without the need for  any  kind  of  embedded  mark-up.  The  module
recognizes Internet quoting conventions, a wide range  of  bulleting
and  number  schemes,  centred  text,  and  block  quotations,   and
reformats each appropriately. Other options allow the user to adjust
inter-word and inter-paragraph spacing,  justify  text,  and  impose
various capitalization schemes.

The  module  also  supplies  a   re-entrant,   highly   configurable
replacement for the built-in Perl format() mechanism.

%prep
%setup -q -n %{module}-%{version}
bzcat %{SOURCE1} > dot-vimrc
bzcat %{SOURCE2} > dot-emacs

%build

CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT

eval `perl '-V:installarchlib'`
install -d $RPM_BUILD_ROOT/$installarchlib

#{__make} PREFIX=$RPM_BUILD_ROOT%{_prefix} install
%makeinstall_std

install -d $RPM_BUILD_ROOT/%{_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes dot-vimrc dot-emacs
%{perl_vendorlib}/Text/*
%{_mandir}/*/*
