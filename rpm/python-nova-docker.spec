%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:          python-nova-docker
Version:       16.04
Release:       4%{?dist}
Summary:       Docker driver for OpenStack Nova
Source:        %name-%version.tar.gz

License:       ASL 2.0

BuildArch:     noarch
BuildRequires: python-devel
BuildRequires: python-setuptools
Requires:      python-pbr
Requires:      python-babel
Requires:      python-six
Requires:      python-oslo-serialization
Requires:      python-oslo-utils
Requires:      python-oslo-config
Requires:      python-oslo-concurrency
Requires:      python-oslo-i18n
Requires:      python-docker-py


%description
Docker driver for OpenStack Nova


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
