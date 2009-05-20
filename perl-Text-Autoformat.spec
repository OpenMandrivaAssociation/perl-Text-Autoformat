%define module	Text-Autoformat
%define version 1.666.0
%define release	%mkrel 1

Name:		perl-%{module}
Version:	%{version}
Release:	%{release}
Summary:	Automatic text wrapping and reformatting
License:	Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Text/%{module}-%{version}.tar.gz
Source1:	dot-vimrc.bz2
Source2:	dot-emacs.bz2
BuildRequires:	perl-Text-Reform
Requires:       perl-Text-Reform
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes dot-vimrc dot-emacs
%{perl_vendorlib}/Text
%{_mandir}/*/*
