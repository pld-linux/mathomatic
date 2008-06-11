Summary:	Mathomatic - a symbolic math program
Summary(pl.UTF-8):	Mathomatic - program do matematyki symbolicznej
Name:		mathomatic
Version:	14.0.4
Release:	1
License:	LGPL
Group:		Applications/Math
Source0:	http://www.panix.com/~gesslein/%{name}-%{version}.tar.bz2
# Source0-md5:	1f16d109e578f8731e16530d81aa9dab
URL:		http://www.mathomatic.com/math/
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mathomatic is a symbolic math program that can automatically solve,
simplify, differentiate, combine, and compare algebraic equations,
perform polynomial and complex arithmetic, etc. The C source code is
available for a UNIX/Linux freeware version. It was written by George
Gesslein II and has been under development since 1986.

%description -l pl.UTF-8
Mathomatic jest pakietem do obliczeń w matematyce symbolicznej, który
może automatycznie rozwiązywać, upraszczać, różnicować, kombinować
i porównywać równania algebraiczne. Kod w C jest dostępny darmowo dla
środowisk UNIX/Linux. Został napisany przez George Gesslein II i jest
rozwijany od roku 1986.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -DUNIX -DREADLINE -DVERSION=\\"\"%{version}\\"\"" \
	LDFLAGS="%{rpmldflags}" \
	LIBS="-lm -lreadline"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}

install -D %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt doc/*.html
%attr(755,root,root) %{_bindir}/*
%{_examplesdir}/%{name}
