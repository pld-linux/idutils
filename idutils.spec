# maybe TODO: emacs stuff
Summary:	ID database utilities
Summary(pl.UTF-8):	Narzędzia do bazy danych identyfikatorów
Name:		idutils
Version:	4.6
Release:	2
License:	GPL v3+
Group:		Applications
Source0:	http://ftp.gnu.org/gnu/idutils/%{name}-%{version}.tar.xz
# Source0-md5:	99b572536377fcddb4d38e86a3c215fd
Patch0:		%{name}-info.patch
Patch1:		%{name}-pl.po-update.patch
Patch2:		stdio.patch
URL:		http://www.gnu.org/software/idutils/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake >= 1:1.11
BuildRequires:	gettext-tools >= 0.18
BuildRequires:	tar >= 1:1.22
BuildRequires:	texinfo
BuildRequires:	xz
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
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/aid
%attr(755,root,root) %{_bindir}/defid
%attr(755,root,root) %{_bindir}/eid
%attr(755,root,root) %{_bindir}/fid
%attr(755,root,root) %{_bindir}/fnid
%attr(755,root,root) %{_bindir}/gid
%attr(755,root,root) %{_bindir}/lid
%attr(755,root,root) %{_bindir}/mkid
%attr(755,root,root) %{_bindir}/xtokid
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/id-lang.map
%{_mandir}/man1/aid.1*
%{_mandir}/man1/defid.1*
%{_mandir}/man1/eid.1*
%{_mandir}/man1/fid.1*
%{_mandir}/man1/fnid.1*
%{_mandir}/man1/gid.1*
%{_mandir}/man1/lid.1*
%{_mandir}/man1/mkid.1*
%{_mandir}/man1/xtokid.1*
%{_infodir}/idutils.info*
