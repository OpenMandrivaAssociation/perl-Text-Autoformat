%define upstream_name	 Text-Autoformat
%define upstream_version 1.669002

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Automatic text wrapping and reformatting
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz
Source1:	dot-vimrc.bz2
Source2:	dot-emacs.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Text::Reform)

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
%setup -q -n %{upstream_name}-%{upstream_version}
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
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.669.2-5mdv2012.0
+ Revision: 765754
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.669.2-4
+ Revision: 764259
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.669.2-3
+ Revision: 667394
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 1.669.2-2mdv2011.0
+ Revision: 564757
- rebuild for perl 5.12.1

* Tue Jul 13 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.669.2-1mdv2011.0
+ Revision: 552640
- update to 1.669002

* Tue Apr 06 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.668.1-1mdv2010.1
+ Revision: 532161
- update to 1.668001

* Thu May 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.666.0-1mdv2010.0
+ Revision: 378142
- new version

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.14.0-2mdv2009.0
+ Revision: 265437
- rebuild early 2009.0 package (before pixel changes)

* Sun Mar 09 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.14.0-1mdv2009.0
+ Revision: 183114
- new version

* Tue Jan 22 2008 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.13-6mdv2008.1
+ Revision: 156507
- force 5.10.0 rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 1.13-5mdv2008.0
+ Revision: 67533
- rebuild

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 1.13-4mdv2008.0
+ Revision: 23308
- rebuild

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 1.13-3mdv2008.0
+ Revision: 23306
- rebuild


* Mon Feb 27 2006 Stefan van der Eijk <stefan@eijk.nu> 1.13-2mdk
- use %%makeinstall_std

* Fri May 27 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.13-1mdk
- 1.13
- Make rpmbuildable

* Tue Jul 27 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.12-2mdk
- rebuild

* Sat Jun 14 2003 Han Boetes <han@linux-mandrake.com> 1.12-1mdk
- Bump

* Thu May 15 2003 Han Boetes <han@linux-mandrake.com> 1.11-1mdk
- Bump

* Fri Apr 25 2003 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.04-9mdk
- fixed buildrequires (Stefan van der Eijk <stefan@eijk.nu>)

