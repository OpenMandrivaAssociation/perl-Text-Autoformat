%define modname	Text-Autoformat

Summary:	Automatic text wrapping and reformatting
Name:		perl-%{modname}
Version:	1.75
Release:	1
License:	Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Text::Autoformat
Source0:	http://www.cpan.org/modules/by-module/Text/%{modname}-%{version}.tar.gz
Source1:	dot-vimrc.bz2
Source2:	dot-emacs.bz2
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
BuildRequires:	perl(Text::Reform)

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
%autosetup -p1 -n %{modname}-%{version}
bzcat %{SOURCE1} > dot-vimrc
bzcat %{SOURCE2} > dot-emacs

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
%make test

%install
%make_install

%files
%doc README Changes dot-vimrc dot-emacs META.yml
%{perl_vendorlib}/Text
%{_mandir}/man3/*
