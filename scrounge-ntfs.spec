Summary:	Data recovery program for NTFS file systems
Summary(pl):	Program odzyskuj±cy dane z systemu plików NTFS
Name:		scrounge-ntfs
Version:	0.8.6
Release:	0.1
License:	BSD
Group:		Applications/System
Source0:	http://memberwebs.com/nielsen/software/scrounge/%{name}-%{version}.tar.gz
# Source0-md5:	573b57e10557923f622786028c488815
Patch0:		%{name}-configure.patch
URL:		http://memberwebs.com/nielsen/software/scrounge/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scrounge NTFS is a data recovery program for NTFS filesystems. It
reads each block of a hard disk and rebuilds the filesystem tree on
another partition.

%description -l pl
Scrounge NTFS jest programem s³u¿±cym do odzyskiwania danych z
partycji NTFS. Scrounge NTFS czyta ka¿dy blok twardego dysku i
przebudowuje strukturê katalogów na inn± partycjê.

%prep
%setup -q
%patch0 -p0

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_sbindir}/scrounge-ntfs
%{_mandir}/man8/*
