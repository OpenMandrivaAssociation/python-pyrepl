%define module pyrepl
# disable tests
%bcond_with test

Name:		python-pyrepl
Version:	0.11.5
Release:	1
Summary:	A library for building flexible command line interfaces
URL:		https://pypi.org/project/pyrepl/
License:	MIT
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/p/pyrepl/pyrepl-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with test}
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pexpect)
%endif

%description
A library for building flexible command line interfaces.

%prep -a
# pythoni1's entry point names pyrepl.python1. The module is pythoni1.
sed -i 's/pyrepl\.python1:main/pyrepl.pythoni1:main/' pyproject.toml

%build -p
# The sdist is not a git checkout.
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%if %{with test}
%check
#%%{__python} -m
pytest -v testing/ -p no:unraisableexception -k 'not (test_raw_input or test_read_history_file)'
%endif

%files
%{_bindir}/pythoni
%{_bindir}/pythoni1

%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}*.*-info
%license LICENSE
%doc README.md
