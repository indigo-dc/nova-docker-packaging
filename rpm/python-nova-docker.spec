%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:          python-nova-docker
Version:       13.0.0~indigo
Release:       1%{?dist}
Summary:       Docker driver for OpenStack Nova Compute
Source:        %name-%version.tar.gz

License:       ASL 2.0

BuildArch:     noarch
BuildRequires: python-devel
BuildRequires: python-setuptools
Requires:      docker-engine
Requires:      openstack-nova-compute >= 13.0.0
Requires:      python-nova >= 13.0.0
Requires:      python-docker-py
Requires:      python-pbr
Requires:      python-babel
Requires:      python-six
Requires:      python-oslo-serialization
Requires:      python-oslo-utils
Requires:      python-oslo-config
Requires:      python-oslo-concurrency
Requires:      python-oslo-i18n
Conflicts:     python-nova-docker = 16.04

%description
OpenStack Compute - compute node (Docker)
OpenStack is a reliable cloud infrastructure. Its mission is to produce the
ubiquitous cloud computing platform that will meet the needs of public and
private cloud providers regardless of size, by being simple to implement and
massively scalable.

OpenStack Compute, codenamed Nova, is a cloud computing fabric controller. In
addition to its "native" API (the OpenStack API), it also supports the Amazon
EC2 API.

Nova is intended to be modular and easy to extend and adapt. It supports many
different hypervisors (KVM and Xen to name a few), different database backends
(SQLite, MySQL, and PostgreSQL, for instance), different types of user
databases (LDAP or SQL), etc.

Install this package on your compute nodes if you're using Docker.


%prep
%setup -q


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%files
%doc README.rst
%{python_sitelib}/*


%changelog
* Mon Jan 16 2017 Vincent Llorens <vincent.llorens@cc.in2p3.fr> - 13.0.0~indigo-1
- Update OpenStack dependency to Mitaka.

* Fri Aug 29 2016 Vincent Llorens <vincent.llorens@cc.in2p3.fr> - 12.0.4~indigo-1
- Fix dependencies and versioning

