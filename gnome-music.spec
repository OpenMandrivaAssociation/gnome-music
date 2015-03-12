%define url_ver %(echo %{version}|cut -d. -f1,2)

Name:		gnome-music
Version:	3.15.91
Release:	1
Summary:	Music player and management application
License:	GPLv2+
Group:		Sound
URL:		https://wiki.gnome.org/Design/Apps/Music
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	python3
BuildRequires:	pkgconfig(gobject-introspection-1.0) >= 1.35.9
BuildRequires:	pkgconfig(grilo-0.2) >= 0.2.6
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.8
BuildRequires:	itstool
BuildRequires:	libxml2-utils
Requires:	gnome-settings-daemon
Requires:	grilo
Requires:	python3-dbus
Requires:	python3-gobject3
Requires:	tracker
Suggests:	grilo-plugins
Requires:	typelib(TotemPlParser)
Requires:	typelib(Grl)
Requires:	python3-gi-cairo

%description
Music is the new GNOME music playing application.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

find %{buildroot} -name '*.la' -delete

%find_lang %{name}

%files -f %{name}.lang
%doc README NEWS
%{_bindir}/%{name}
%{_libdir}/%{name}
%{py3_puresitedir}/gnomemusic
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/%{name}
%{_iconsdir}/*/*/*/*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/help/*/gnome-music/*

