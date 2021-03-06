Summary:	Mathomatic - a symbolic math program
Summary(hu.UTF-8):	Mathomatic - szimbolikus számításokra képes program
Summary(pl.UTF-8):	Mathomatic - program do matematyki symbolicznej
Name:		mathomatic
Version:	16.0.0
Release:	3
License:	LGPL
Group:		Applications/Math
Source0:	http://www.panix.com/~gesslein/%{name}-%{version}.tar.bz2
# Source0-md5:	a349471e997afcfa222964692780b567
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

%description -l hu.UTF-8
Mathomatic egy szimbolikus számításokra képes program, amely
automatikus megold, egyszerűsít, differenciál, kombinál és hasonlít
össze algebrai egyenleteket, ismeri polinomikus és komplex
aritmetikát, stb. A C forráskód elérhető UNIX/Linux-ra. George
Gesslein II írta, és 1986 óta fejlesztik.

%description -l pl.UTF-8
Mathomatic jest pakietem do obliczeń w matematyce symbolicznej, który
może automatycznie rozwiązywać, upraszczać, różnicować, kombinować i
porównywać równania algebraiczne. Kod w C jest dostępny darmowo dla
środowisk UNIX/Linux. Został napisany przez George Gesslein II i jest
rozwijany od roku 1986.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -DUNIX -DREADLINE -DVERSION=\\"\"%{version}\\"\" -I%{_includedir}/ncurses" \
	LDFLAGS="%{rpmldflags}" \
	LDLIBS="-lm -lreadline -ltinfow" \
	READLINE=1

%install
rm -rf $RPM_BUILD_ROOT
install -D %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt doc/*.html
%attr(755,root,root) %{_bindir}/*
