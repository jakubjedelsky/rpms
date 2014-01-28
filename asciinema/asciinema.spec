%if 0%{?rhel}
%global __python2 %{__python}
%global python2_sitelib %{python_sitelib}
%endif

Name:		asciinema
Version:	0.9.7
Release:	4%{?dist}
Summary:	Command line recorder for asciinema.org service

Group:		Applications/Internet
License:	MIT
URL:		http://asciinema.org
Source0:	https://github.com/sickill/%{name}/archive/v%{version}.tar.gz
# https://github.com/sickill/asciinema/issues/51
Patch1:		asciinema-0.9.7-pty-recorder.patch

BuildArch:	noarch

BuildRequires:	python-setuptools
BuildRequires:	python2-devel
BuildRequires:	python-nose
BuildRequires:	python-requests >= 1.1.0
BuildRequires:	ncurses
Requires:	python-requests >= 1.1.0
Requires:	ncurses


%description
Asciinema is a free and open source solution for recording the terminal sessions
and sharing them on the web.


%prep
%setup -q
%patch1 -p1


%build
%{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root $RPM_BUILD_ROOT


%check
nosetests tests/*_test.py


%files
%doc LICENSE.txt README.md config.example
%{_bindir}/asciinema
%{python2_sitelib}/*.egg-info
%dir %{python2_sitelib}/%{name}
%{python2_sitelib}/%{name}/*


%changelog
* Tue Jan 28 2014 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.9.7-7
- Add support for EPEL6

* Mon Jan 27 2014 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.9.7-3
- Add check of tests
- Add build and common requires
- Patch for non-interactive shell

* Mon Dec  2 2013 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.9.7-2
- A few spec file changes

* Mon Nov 25 2013 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.9.7-1
- Initial package
