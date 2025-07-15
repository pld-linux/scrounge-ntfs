Summary:	Data recovery program for NTFS file systems
Summary(pl.UTF-8):	Program odzyskujący dane z systemu plików NTFS
Name:		scrounge-ntfs
Version:	0.9
Release:	1
License:	BSD
Group:		Applications/System
Source0:	http://memberwebs.com/nielsen/software/scrounge/%{name}-%{version}.tar.gz
# Source0-md5:	851cbb9a1ce417cf61f2612626a1bc58
Patch0:		%{name}-configure.patch
URL:		http://memberwebs.com/nielsen/software/scrounge/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scrounge NTFS is a data recovery program for NTFS filesystems. It
reads each block of a hard disk and rebuilds the filesystem tree on
another partition.

%description -l pl.UTF-8
Scrounge NTFS jest programem służącym do odzyskiwania danych z
partycji NTFS. Scrounge NTFS czyta każdy blok twardego dysku i
przebudowuje strukturę katalogów na inną partycję.

%prep
%setup -q
%patch -P0 -p0

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
