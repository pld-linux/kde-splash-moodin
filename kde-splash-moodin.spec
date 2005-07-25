
%define		_splash		moodin

Summary:	KDE splash screen
Summary(pl):	Ekran startowy KDE
Name:		kde-splash-%{_splash}
Version:	0.4.2
Release:	1
License:	GPL
Group:		X11/Amusements
Source0:	http://moodwrod.com/files/ksplash-engine-%{_splash}_%{version}.tar.gz
# Source0-md5:	322404928ed7e17a1c8708d4dc13b960
URL:		http://www.kde-look.org/content/show.php?content=25705
Requires:	kdebase-desktop >= 9:3.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a new splash screen engine for KDE 3.4. It includes the
moodinn and FingerPrint theme.

Featues:
 - Fading icons
 - Use current icon set or custom images
 - Use custom text values
 - Set fading delay and length
 - Custom icon/image arrangement

%description -l pl
To jest nowy silnik ekranu startowego dla KDE 3.4. Zawiera motywy
moodin i FingerPrint.

Cechy:
 - wygasaj±ce ikony
 - u¿ycie aktualnego zestawu ikon lub w³asnych obrazków
 - u¿ycie w³asnych warto¶ci tekstu
 - ustawianie opó¼nienia i d³ugo¶ci wygasania
 - w³asny uk³ad ikon/obrazków

%prep
%setup -q -n %{_splash}

%build

%configure \
        --with-qt-libraries=%{_libdir}
%{__make}

%install

%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/kde3/ksplashmoodin.*
%{_datadir}/apps/ksplash/Themes/MoodinKDE
%{_datadir}/apps/ksplash/Themes/FingerPrint
%{_datadir}/services/ksplashmoodin.desktop
