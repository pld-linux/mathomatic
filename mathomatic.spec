Summary:	Mathomatic - a symbolic math program
Summary(pl):	Mathomatic - program do matematyki symbolicznej
Name:		mathomatic
Version:	10.5
Release:	1
License:	Freeware
Group:		Applications/Math
Source0:	ftp://ftp.lightlink.com/pub/computer/math/am.zip
# Source0-md5:	1b5261e883646f379ceeee7a9cb6e45d
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
Mathomatic jest pakietem do obliczeñ w matematyce symbolicznej który
mo¿e automatycznie rozwi±zywaæ, upraszaszczaæ, ró¿nicowaæ, kombinowaæ
i porównywaæ równania algebraiczne. Kod w C jest dostêpny darmowo dla
¶rodowisk UNIX/Linux. Zosta³ napisany przez Gorge Gesslein II i jest
rozwijany od roku 1986.

%prep
%setup -q -c
for i in *; do mv "$i" "`echo $i |tr A-Z a-z`";done

%build
%{__make} \
	CFLAGS="%{rpmcflags} -DUNIX -DREADLINE -c" \
	LFLAGS="-lreadline"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}

install -D ac $RPM_BUILD_ROOT%{_bindir}/am
install -D am.1 $RPM_BUILD_ROOT%{_mandir}/man1/am.1
echo ".so am.1" > $RPM_BUILD_ROOT%{_mandir}/man1/amc.1
install *.in $RPM_BUILD_ROOT%{_examplesdir}/%{name}

cat <<EOF >$RPM_BUILD_ROOT%{_bindir}/amc
#!/bin/sh
am -c
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt *.htm
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_examplesdir}/%{name}
