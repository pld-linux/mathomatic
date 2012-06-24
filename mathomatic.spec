Summary:	Mathomatic - a symbolic math program
Summary(pl):	Mathomatic - program do matematyki symbolicznej
Name:		mathomatic
Version:	12.3.3
Release:	1
License:	LGPL
Group:		Applications/Math
Source0:	http://www.panix.com/~gesslein/%{name}-%{version}.tgz
# Source0-md5:	08fe86615fad0708f2aabf0e82ad2c31
URL:		http://www.mathomatic.com/
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mathomatic is a symbolic math program that can automatically solve,
simplify, differentiate, combine, and compare algebraic equations,
perform polynomial and complex arithmetic, etc. The C source code is
available for a UNIX/Linux freeware version. It was written by George
Gesslein II and has been under development since 1986.

%description -l pl
Mathomatic jest pakietem do oblicze� w matematyce symbolicznej, kt�ry
mo�e automatycznie rozwi�zywa�, upraszcza�, r�nicowa�, kombinowa�
i por�wnywa� r�wnania algebraiczne. Kod w C jest dost�pny darmowo dla
�rodowisk UNIX/Linux. Zosta� napisany przez George Gesslein II i jest
rozwijany od roku 1986.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -DUNIX -DREADLINE -DVERSION=\\"\"%{version}\\"\"" \
	LDFLAGS="%{rpmldflags} -lreadline"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}

install -D %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D doc/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt doc/*.htm
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_examplesdir}/%{name}
