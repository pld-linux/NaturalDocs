%include	/usr/lib/rpm/macros.perl
Summary:	Multi-language documentation generator
Summary(pl):	Wielojêzykowy generator dokumentacji
Name:		NaturalDocs
Version:	1.16
Release:	1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/naturaldocs/%{name}-%{version}.zip
# Source0-md5:	7c1a8aac0e239223e4e30e67b224eb99
Patch0:		%{name}-path.patch
URL:		http://www.naturaldocs.org/
BuildRequires:	perl-modules >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Natural Docs is an open-source, extensible, multi-language
documentation generator. It extracts specially formatted comments from
source code and builds HTML documentation from it. The syntax is
transparent so that the comments in the source code read just as
easily as the generated documentation. It also focuses on automation
and high-quality generated output.

%description -l pl
Natural Docs jest ³atwo rozszerzalnym, wielojêzykowym generatorem
dokumentacji o otwartym kodzie ¼ród³owym. Wyci±ga on odpowiednio
sformatowane komentarze z kodu ¼ród³owego i tworzy z nich dokumentacjê
w postaci HTML-u. Sk³adnia jest przezroczysta, wiêc komentarze
wewn±trz kodu ¼ród³owego s± równie ³atwe do przeczytania jak i
wygenerowana dokumentacja. Natural Docs koncentruje siê tak¿e na
wysokiej jako¶ci wygenerowanej dokumentacji.

%prep
%setup -q -c
%patch0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_bindir},%{perl_vendorlib}}

mv Modules/%{name} $RPM_BUILD_ROOT%{perl_vendorlib}
mv Styles $RPM_BUILD_ROOT%{_datadir}/%{name}
install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CSSGuide.txt NDMarkup.txt Help/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{perl_vendorlib}/%{name}
