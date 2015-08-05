%global sname oslo.sphinx

Name:       python-oslo-sphinx
Version:    XXX
Release:    XXX
Summary:    OpenStack Sphinx Extensions

License:    ASL 2.0
URL:        https://launchpad.net/oslo
Source0:    http://tarballs.openstack.org/%{sname}/%{sname}-%{version}.tar.gz

BuildArch:  noarch
Requires:   python-setuptools

BuildRequires: python2-devel
BuildRequires: python-setuptools
BuildRequires: python-d2to1
BuildRequires: python-pbr

Requires:      python-requests >= 2.5.2
Requires:      python-pbr

%description
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

The oslo-sphinx library contains Sphinx theme and extensions support used by
OpenStack.

%prep
%setup -q -n oslosphinx-%{upstream_version}
# Remove bundled egg-info
rm -rf oslo_sphinx.egg-info

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

%files
%license LICENSE
%doc README.rst
%{python2_sitelib}/oslosphinx
%{python2_sitelib}/oslosphinx*.egg-info

%changelog
