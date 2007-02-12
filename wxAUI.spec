# TODO: optflags

%bcond_with	unicode		# use wx-gtk2-unicode-config instead of wx-gtk2-ansi-config

Summary:	wxAUI - an Advanced User Interface library for wxWidgets
Summary(pl.UTF-8):	wxAUI - zaawansowana biblioteka interfejsu użytkownika dla wxWidgets
Name:		wxAUI
Version:	0.9.1
Release:	1
License:	wxWindows
Group:		Libraries
Source0:	wxaui-%{version}.tar.gz
# Source0-md5:	a2125352cd2b2415954294b7b726ca41
Source1:	http://www.alex.org.uk/wxAUI/%{version}/wxaui.tgz
# Source1-md5:	dbf79fcd99c12335578718aa7579210b
Patch0:		%{name}-Makefile.patch
URL:		http://www.kirix.com/en/community/opensource/wxaui/about_wxaui.html
BuildRequires:	wxGTK2-%{?with_unicode:unicode-}devel >= 2.6.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	wxwidgets_ver	2.6

%description
wxAUI is an Advanced User Interface library that aims to implement
"cutting-edge" interface usability and design features so developers
can quickly and easily create beautiful and usable application
interfaces.

%description -l pl.UTF-8
wxAUI jest zaawansowaną biblioteką interfejsu użytkownika pozwalającą
programistom szybko i łatwo zaprojektować profesjonalnie wyglądający i
wygodny w użytkowaniu interfejs.

%package devel
Summary:	Header files for wxAUI library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki wxAUI
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	wxGTK2-%{?with_unicode:unicode-}devel >= 2.6.1

%description devel
Header files for wxAUI library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki wxAUI.

%package static
Summary:	Static wxAUI library
Summary(pl.UTF-8):	Statyczna biblioteka wxAUI
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static wxAUI library.

%description static -l pl.UTF-8
Statyczna biblioteka wxAUI.

%package sample
Summary:	Sample application using wxAUI library
Summary(pl.UTF-8):	Przykładowa aplikacja używająca biblioteki wxAUI
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description sample
Sample application using wxAUI library.

%description sample -l pl.UTF-8
Przykładowa aplikacja używająca biblioteki wxAUI.

%prep
%setup -q -n wxaui-%{version}
dos2unix Makefile sample/Makefile
%patch0 -p1

# a nasty hack to apply Alex' patches
ln -s src wxXtra
zcat %{SOURCE1} | tar xO | patch -p0
rm -f wxXtra

%build
%{__make} \
	WXCONFIG="wx-gtk2-%{?with_unicode:unicode}%{!?with_unicode:ansi}-config"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}/wx-%{wxwidgets_ver}/wx}

install lib/libwxaui.* $RPM_BUILD_ROOT%{_libdir}
install include/*.h $RPM_BUILD_ROOT%{_includedir}/wx-%{wxwidgets_ver}/wx
install sample/wxauitest $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/wx-%{wxwidgets_ver}/wx/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files sample
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/wxauitest
