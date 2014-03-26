%if 0%{?fedora}
%global _with_python3 1
%else
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

Name:           vertica-python
Version:        0.2.0
Release:        2%{?dist}
Summary:        A native Python adapter for the Vertica database

Group:          Development/Languages
License:        MIT
URL:            https://github.com/uber/vertica-python
Source0:        https://github.com/uber/vertica-python/archive/%{version}.tar.gz
Patch0:         vertica-python-0.2.0-python3.patch
Patch1:         vertica-python-0.2.0-version.patch
# EPEL 6 patch
Patch2:         vertica-python-0.2.0-dateutil15.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-pip

%if 0%{?rhel} <= 6
Requires:       python-dateutil15
Requires:       python-setuptools
%else
Requires:       python-dateutil
%endif

Requires:       pytz
Requires:       python-psycopg2

%if 0%{?_with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-dateutil
BuildRequires:  python3-pytz

Requires:       python3-dateutil
Requires:       python3-pytz
Requires:       python3-psycopg2
%endif


%description
vertica-python is a native Python adapter for the Vertica
(http://www.vertica.com) database.

%if 0%{?_with_python3}
%package -n vertica-python3
Summary:        A native Python3 adapter for the Vertica database


%description -n vertica-python3
vertica-python3 is a native Python adapter for the Vertica
(http://www.vertica.com) database.
%endif


%prep
%setup -q -n vertica-python-%{version}
%patch0 -p1
%patch1 -p1

%if 0%{?rhel} <= 6
%patch2 -p1
%endif

%if 0%{?_with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif


%build
%{__python2} setup.py build

%if 0%{?_with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif


%install
%if 0%{?_with_python3}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root $RPM_BUILD_ROOT
popd
%endif

%{__python2} setup.py install --skip-build --root $RPM_BUILD_ROOT

 
%files
%doc README.md LICENSE
%{python2_sitelib}/*.egg-info
%dir %{python2_sitelib}/vertica_python
%{python2_sitelib}/vertica_python/*

%if 0%{?_with_python3}
%files -n vertica-python3
%doc README.md LICENSE
%{python3_sitelib}/*.egg-info
%dir %{python3_sitelib}/vertica_python
%{python3_sitelib}/vertica_python/*
%endif


%changelog
* Wed Mar 26 2014 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.2.0-2
- python-setuptools is required only on rhel<=6

* Mon Mar 24 2014 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.2.0-1
- Initial package
