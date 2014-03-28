%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:           vertica-python
Version:        0.2.0
Release:        4%{?dist}
Summary:        A native Python adapter for the Vertica database

Group:          Development/Languages
License:        MIT
URL:            https://github.com/uber/vertica-python
Source0:        https://github.com/uber/vertica-python/archive/%{version}.tar.gz
Patch0:         vertica-python-0.2.0-version.patch
# EPEL 6 patch
Patch1:         vertica-python-0.2.0-dateutil15.patch

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-pip

%if 0%{?rhel} <= 6
Requires:       python-dateutil15
Requires:       python-setuptools
%else
Requires:       python-dateutil >= 1.5
%endif

Requires:       pytz
Requires:       python-psycopg2


%description
vertica-python is a native Python adapter for the Vertica
(http://www.vertica.com) database.


%prep
%setup -q -n vertica-python-%{version}
%patch0 -p1

%if 0%{?rhel} <= 6
%patch1 -p1
%endif


%build
%{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root $RPM_BUILD_ROOT

 
%files
%doc README.md LICENSE
%{python2_sitelib}/*.egg-info
%dir %{python2_sitelib}/vertica_python
%{python2_sitelib}/vertica_python/*


%changelog
* Fri Mar 28 2014 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.2.0-4
- remove buildrood tag
- edit dateutil patch for el6

* Wed Mar 26 2014 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.2.0-3
- package is not ready for python3 

* Wed Mar 26 2014 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.2.0-2
- python-setuptools is required only on rhel<=6

* Mon Mar 24 2014 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.2.0-1
- Initial package
