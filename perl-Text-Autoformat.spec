%define upstream_name	 Text-Autoformat
%define upstream_version 1.669002

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	Automatic text wrapping and reformatting
License:	Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz
Source1:	dot-vimrc.bz2
Source2:	dot-emacs.bz2

BuildRequires:	perl(Text::Reform)

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
%setup -q -n %{upstream_name}-%{upstream_version}
bzcat %{SOURCE1} > dot-vimrc
bzcat %{SOURCE2} > dot-emacs

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes dot-vimrc dot-emacs META.yml
%{perl_vendorlib}/Text
%{_mandir}/*/*
