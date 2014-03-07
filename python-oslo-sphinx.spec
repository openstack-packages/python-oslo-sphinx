%global sname oslosphinx

Name:       python-oslo-sphinx
Version:    2.0
Release:    1%{?dist}
Summary:    OpenStack Sphinx Extensions

Group:      Development/Languages
License:    ASL 2.0
URL:        https://launchpad.net/oslo
Source0:    http://tarballs.openstack.org/%{sname}/%{sname}-%{version}.tar.gz

BuildArch:  noarch
Requires:   python-setuptools

BuildRequires: python2-devel
BuildRequires: python-setuptools
BuildRequires: python-pbr
BuildRequires: python-d2to1

%description
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

The oslo-sphinx library contains Sphinx theme and extensions support used by
OpenStack.

%prep
%setup -q -n %{sname}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

%files
%doc LICENSE README.rst
%{python_sitelib}/%{sname}
%{python_sitelib}/*.egg-info

%changelog
* Fri Mar 07 2014 Pádraig Brady <pbrady@redhat.com> 2.0-1
- Latest upstream

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Pádraig Brady <pbrady@redhat.com> 1.0-3
- Review adjustments

* Mon Jul 8 2013 Dan Prince <dprince@redhat.com> 1.0-1
- Initial package.
