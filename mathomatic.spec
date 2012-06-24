Summary:	Mathomatic - a symbolic math program
Summary(pl):	Mathomatic - program do matematyki symbolicznej
Name:		mathomatic
Version:	11.1
Release:	2
License:	LGPL
Group:		Applications/Math
Source0:	http://www.panix.com/~gesslein/%{name}-%{version}.tgz
# Source0-md5:	c09f8ede798f8239cdd7c2667ef9ac38
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
Mathomatic jest pakietem do oblicze� w matematyce symbolicznej kt�ry
mo�e automatycznie rozwi�zywa�, upraszaszcza�, r�nicowa�, kombinowa�
i por�wnywa� r�wnania algebraiczne. Kod w C jest dost�pny darmowo dla
�rodowisk UNIX/Linux. Zosta� napisany przez George Gesslein II i jest
rozwijany od roku 1986.

%prep
%setup -q -n am

%build
%{__make} \
	CC=%{__cc} \
	CFLAGS="%{rpmcflags} -DUNIX -DREADLINE -c" \
	LDFLAGS="%{rpmldflags} -lreadline"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}

install -D am $RPM_BUILD_ROOT%{_bindir}/am
install -D am.1 $RPM_BUILD_ROOT%{_mandir}/man1/am.1
echo ".so am.1" > $RPM_BUILD_ROOT%{_mandir}/man1/amc.1

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
