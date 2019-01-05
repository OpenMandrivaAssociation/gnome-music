%define _disable_rebuild_configure 1
%define url_ver %(echo %{version}|cut -d. -f1,2)

Name:		gnome-music
Version:	3.30.1
Release:	1
Summary:	Music player and management application
License:	GPLv2+
Group:		Sound
URL:		https://wiki.gnome.org/Design/Apps/Music
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	python3
BuildRequires:	pkgconfig(goa-1.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0) >= 1.35.9
BuildRequires:	pkgconfig(grilo-0.3)
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.8
BuildRequires:	pkgconfig(libmediaart-2.0)
BuildRequires:	pkgconfig(tracker-sparql-2.0)
BuildRequires:  pkgconfig(libdazzle-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:	itstool
BuildRequires:	libxml2-utils
BuildRequires:	meson
Requires:	gnome-settings-daemon
Requires:	grilo
Requires:	python-dbus
Requires:	python-gi
Requires:	tracker
Suggests:	grilo-plugins

%description
Music is the new GNOME music playing application.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

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
%{_mandir}/man1/%{name}.1*

