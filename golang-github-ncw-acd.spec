# Run tests in check section
%bcond_without check

%global goipath         github.com/ncw/go-acd
%global commit          887eb06ab6a255fbf5744b5812788e884078620a

%global common_description %{expand:
Go library for accessing the Amazon Cloud Drive.}

%gometa

Name:    %{goname}
Version: 0
Release: 0.4%{?dist}
Summary: Go library for accessing the Amazon Cloud Drive
License: ISC
URL:     %{gourl}
Source:  %{gosource}

BuildRequires: golang(github.com/google/go-querystring/query)

%if %{with check}
BuildRequires: golang(github.com/stretchr/testify/assert)
%endif

%description
%{common_description}


%package    devel
Summary:    %{summary}
BuildArch:  noarch

Provides: golang-github-ncw-go-acd-devel = %{version}-%{release}
Obsoletes: golang-github-ncw-go-acd-devel < 0-0.3.20180314git887eb06
 
%description devel
%{common_description}
 
This package contains the source code needed for building packages that import
the %{goipath} Go namespace.


%prep
%gosetup -q


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.git887eb06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 08 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20180320git887eb06
- Update with the new Go packaging

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20171119git887eb06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 07 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20171119git887eb06
- Upstream GIT revision 887eb06

* Mon Jul 24 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20170306git96a49aa
- First package for Fedora

