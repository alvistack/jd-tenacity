# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-tenacity
Epoch: 100
Version: 8.4.1
Release: 1%{?dist}
BuildArch: noarch
Summary: Retrying library for Python
License: Apache-2.0
URL: https://github.com/jd/tenacity/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Tenacity is an Apache 2.0 licensed general-purpose retrying library,
written in Python, to simplify the task of adding retry behavior to just
about anything. It originates from a fork of retrying which is sadly no
longer maintained. Tenacity isn't api compatible with retrying but adds
significant new functionality and fixes a number of longstanding bugs.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-tenacity
Summary: Retrying library for Python
Requires: python3
Provides: python3-tenacity = %{epoch}:%{version}-%{release}
Provides: python3dist(tenacity) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-tenacity = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(tenacity) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-tenacity = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(tenacity) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-tenacity
Tenacity is an Apache 2.0 licensed general-purpose retrying library,
written in Python, to simplify the task of adding retry behavior to just
about anything. It originates from a fork of retrying which is sadly no
longer maintained. Tenacity isn't api compatible with retrying but adds
significant new functionality and fixes a number of longstanding bugs.

%files -n python%{python3_version_nodots}-tenacity
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-tenacity
Summary: Retrying library for Python
Requires: python3
Provides: python3-tenacity = %{epoch}:%{version}-%{release}
Provides: python3dist(tenacity) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-tenacity = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(tenacity) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-tenacity = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(tenacity) = %{epoch}:%{version}-%{release}

%description -n python3-tenacity
Tenacity is an Apache 2.0 licensed general-purpose retrying library,
written in Python, to simplify the task of adding retry behavior to just
about anything. It originates from a fork of retrying which is sadly no
longer maintained. Tenacity isn't api compatible with retrying but adds
significant new functionality and fixes a number of longstanding bugs.

%files -n python3-tenacity
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
