%define modname	Text-Autoformat
%define modver	1.669002

Summary:	Automatic text wrapping and reformatting
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	10
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Text/%{modname}-%{modver}.tar.gz
Source1:	dot-vimrc.bz2
Source2:	dot-emacs.bz2
BuildArch:	noarch
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
%setup -qn %{modname}-%{modver}
bzcat %{SOURCE1} > dot-vimrc
bzcat %{SOURCE2} > dot-emacs

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes dot-vimrc dot-emacs META.yml
%{perl_vendorlib}/Text
%{_mandir}/man3/*

