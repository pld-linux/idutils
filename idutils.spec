# maybe TODO: emacs stuff
Summary:	ID database utilities
Summary(pl.UTF-8):	Narzędzia do bazy danych identyfikatorów
Name:		id-utils
Version:	3.2d
Release:	2
License:	GPL
Group:		Applications
Source0:	ftp://ftp.enst.fr/pub/gnu/gnits/%{name}-%{version}.tar.gz
# Source0-md5:	1152902c1fff4fadb8a7827ad91a80b0
Patch0:		%{name}-dirs.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-po.patch
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
`mkid' is a simple, fast, high-capacity, language-independent
identifier database tool. Actually, the term `identifier' is too
limiting - `mkid' stores tokens, be they program identifiers of any
form, literal numbers, or words of human-readable text. Database
queries can be issued from the command-line, or from within emacs,
serving as an augmented tags facility.

%description -l pl.UTF-8
mkid to proste, szybkie, o dużej pojemności, niezależne od języka
narzędzie do baz danych identyfikatorów. Właściwie termin
"identyfikator" jest zbyt wąski - mkid przechowuje tokeny, które mogą
być identyfikatorami programu w dowolnej formie, liczbami czy słowami.
Zapytania do bazy danych mogą być wydawane z linii poleceń lub spod
emacsa.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*id
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/id-lang.map
%{_infodir}/*.info*
