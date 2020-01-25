Summary:	Multi-language documentation generator
Summary(pl.UTF-8):	Wielojęzykowy generator dokumentacji
Name:		NaturalDocs
Version:	1.52
Release:	1
License:	GPL
Group:		Applications
Source0:	http://downloads.sourceforge.net/naturaldocs/%{name}-%{version}.zip
# Source0-md5:	68e3982acae57b6befdf9e75b420fd80
Patch0:		%{name}-path.patch
URL:		http://www.naturaldocs.org/
BuildRequires:	iconv
BuildRequires:	perl-modules >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Natural Docs is an open-source, extensible, multi-language
documentation generator. It extracts specially formatted comments from
source code and builds HTML documentation from it. The syntax is
transparent so that the comments in the source code read just as
easily as the generated documentation. It also focuses on automation
and high-quality generated output.

%description -l pl.UTF-8
Natural Docs jest łatwo rozszerzalnym, wielojęzykowym generatorem
dokumentacji o otwartym kodzie źródłowym. Wyciąga on odpowiednio
sformatowane komentarze z kodu źródłowego i tworzy z nich dokumentację
w postaci HTML-u. Składnia jest przezroczysta, więc komentarze
wewnątrz kodu źródłowego są równie łatwe do przeczytania jak i
wygenerowana dokumentacja. Natural Docs koncentruje się także na
wysokiej jakości wygenerowanej dokumentacji.

%prep
%setup -q -c
%patch0 -p0

# And one non-UTF8 one
iconv -f ISO-8859-1 -t UTF-8 Help/example/Default.css > Help/example/Default.css.utf8
touch --reference Help/example/Default.css Help/example/Default.css.utf8
mv Help/example/Default.css.utf8 Help/example/Default.css

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/%{name},%{_datadir}/%{name}/JavaScript,%{_bindir},%{perl_vendorlib}}

mv Modules/%{name} $RPM_BUILD_ROOT%{perl_vendorlib}
mv Styles $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a Config/*.txt $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
cp -a JavaScript/*.js $RPM_BUILD_ROOT%{_datadir}/%{name}/JavaScript
install -p %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Info/CSSGuide.txt Info/NDMarkup.txt Help/*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/Languages.txt
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/Topics.txt
%attr(755,root,root) %{_bindir}/NaturalDocs
%{_datadir}/%{name}
%{perl_vendorlib}/%{name}
