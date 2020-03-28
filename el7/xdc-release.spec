Name: xdc-release
Version: 2.0.0
Release: 1%{?dist}
Summary: XDC-2 (Quasar) Release
License: Apache Software License
Source: %{name}-%{version}.src.tgz
Vendor: eXtreme-DataCloud
Group: System Environment/Libraries
BuildArch: noarch
Requires: yum-protectbase
Requires: yum-priorities
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
#BuildRoot: %{_tmppath}/%{name}-%{version}-build


%description
eXtreme-DataCloud repository files

%prep
%setup -q

%build
#Nothing to build

%install
rm -rf %{buildroot}
make install prefix=%{buildroot}

%clean
rm -rf ${buildroot}

%post
if [ -f /etc/yum/pluginconf.d/priorities.conf ]; then grep -q -e "check_obsoletes" /etc/yum/pluginconf.d/priorities.conf || sed -i -e "/^\[main\]/{G;s/$/\# added by the xdc-release package\\ncheck_obsoletes = 1/;}" /etc/yum/pluginconf.d/priorities.conf; fi

%postun
if [ "$1" = "0" ]; then grep -q -e "xdc-release" /etc/yum/pluginconf.d/priorities.conf && sed -i '/xdc-release/d;/check_obsoletes/d' /etc/yum/pluginconf.d/priorities.conf; fi

%files
%defattr(-,root,root,-)

/etc/xdc-release
/etc/pki/rpm-gpg/RPM-GPG-KEY-indigodc
/etc/yum.repos.d/xdc-2-base.repo
/etc/yum.repos.d/xdc-2-third-party.repo
/etc/yum.repos.d/xdc-2-updates.repo

%changelog
* Thu Nov 13 2019 Cristina Duma <aiftim@infn.it>
- second release
