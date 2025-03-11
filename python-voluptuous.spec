#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Python data validation library
Summary(pl.UTF-8):	Biblioteka Pythona do sprawdzania poprawności danych
Name:		python-voluptuous
# keep 0.13.x here for python2 support
Version:	0.13.1
Release:	3
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/voluptuous/
Source0:	https://files.pythonhosted.org/packages/source/v/voluptuous/voluptuous-%{version}.tar.gz
# Source0-md5:	78d39d2a15e3717ab8d100944da60d11
Patch0:		%{name}-py2-tests.patch
URL:		https://pypi.org/project/voluptuous/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Voluptuous is a Python data validation library. It is primarily
intended for validating data coming into Python as JSON, YAML, etc.

%description -l pl.UTF-8
Voluptuous to biblioteka Pythona do sprawdzania poprawności danych.
Jest przeznaczona głównie do sprawdzania danych pochodzących z
formatów JSON, YAML itp.

%package -n python3-voluptuous
Summary:	Python data validation library
Summary(pl.UTF-8):	Biblioteka Pythona do sprawdzania poprawności danych
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.6

%description -n python3-voluptuous
Voluptuous is a Python data validation library. It is primarily
intended for validating data coming into Python as JSON, YAML, etc.

%description -n python3-voluptuous -l pl.UTF-8
Voluptuous to biblioteka Pythona do sprawdzania poprawności danych.
Jest przeznaczona głównie do sprawdzania danych pochodzących z
formatów JSON, YAML itp.

%prep
%setup -q -n voluptuous-%{version}
%patch -P 0 -p1

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest voluptuous/tests/tests.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest voluptuous/tests/tests.py
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGELOG.md COPYING README.md
%{py_sitescriptdir}/voluptuous
%{py_sitescriptdir}/voluptuous-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-voluptuous
%defattr(644,root,root,755)
%doc CHANGELOG.md COPYING README.md
%{py3_sitescriptdir}/voluptuous
%{py3_sitescriptdir}/voluptuous-%{version}-py*.egg-info
%endif
