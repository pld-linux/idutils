# maybe TODO: emacs stuff
Summary:	ID database utilities
Summary(pl.UTF-8):	Narzędzia do bazy danych identyfikatorów
Name:		idutils
Version:	4.2
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	ftp://ftp.gnu.org/gnu/idutils/%{name}-%{version}.tar.gz
# Source0-md5:	4bbd2cb0d566ab29e41088cc028ad710
Patch0:		%{name}-info.patch
Patch1:		%{name}-pl.po-update.patch
URL:		http://www.gnu.org/software/idutils/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	texinfo
Obsoletes:	id-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_datadir	%{_sysconfdir}

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

%build
%{__gettextize}
%{__aclocal} -I m4
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
