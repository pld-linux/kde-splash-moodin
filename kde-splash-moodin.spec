
%define		_splash		moodin

Summary:	KDE splash screen
Summary(pl):	Ekran startowy KDE
Name:		kde-splash-%{_splash}
Version:	0.3
Release:	0.1
License:	GPL
Group:		X11/Amusements
Source0:	http://moodwrod.com/files/ksplash-engine-%{_splash}_%{version}.tar.gz
# Source0-md5:	0bedd78b9128f34a33f8e17b39012af4
URL:		http://www.kde-look.org/content/show.php?content=25705
Requires:	kdebase-desktop >= 9:3.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Description:
This is a new splash screen engine for KDE 3.4. It includes the
MoodinKDE theme.

Featues:
 - Fading icons
 - Use current icon set or custom images
 - Use custom text values
 - Set fading delay and length
 - Custom icon/image arrangement

%description -l pl
Napisz mnie:)

%prep
%setup -q -n ksplash-engine-moodin

%build

%configure
%{__make}

%install

%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/kde3/ksplashmoodin.*
%{_datadir}/apps/ksplash/Themes/MoodinKDE
%{_datadir}/services/ksplashmoodin.desktop