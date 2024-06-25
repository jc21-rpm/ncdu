%global debug_package %{nil}

Name:           ncdu
Version:        2.4
Release:        1%{?dist}
Summary:        Ncdu is a disk usage analyzer with an ncurses interface
Group:          Applications/System
License:        GPLv2
URL:            https://dev.yorhel.nl/%{name}
Source:         https://dev.yorhel.nl/download/%{name}-%{version}-linux-x86_64.tar.gz

%description
Ncdu is a disk usage analyzer with an ncurses interface. It is designed to find
space hogs on a remote server where you don’t have an entire graphical setup
available, but it is a useful tool even on regular desktop systems. Ncdu aims
to be fast, simple and easy to use, and should be able to run in any minimal
POSIX-like environment with ncurses installed.

%prep
%setup -q -c %{name}-%{version}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
cp %{name} %{buildroot}/usr/bin/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/bin/%{name}

%changelog
* Tue Jun 25 2024 Jamie Curnow <jc@jc21.com> - 2.4-1
- v2.4

* Thu Dec 8 2022 Jamie Curnow <jc@jc21.com> - 2.2.1-1
- Initial spec
