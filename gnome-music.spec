%define _empty_manifest_terminate_build 0
%define _disable_rebuild_configure 1
%define url_ver %(echo %{version}|cut -d. -f1,2)

Name:		gnome-music
Version:	45.1
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
BuildRequires:	pkgconfig(grilo-plugins-0.3)
BuildRequires:	pkgconfig(gtk4)
BuildRequires:	pkgconfig(libmediaart-2.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:	pkgconfig(tracker-sparql-3.0)
BuildRequires:  pkgconfig(libdazzle-1.0)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  pkgconfig(py3cairo)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:	itstool
BuildRequires:	libxml2-utils
BuildRequires:	meson
BuildRequires:  pkgconfig(grilo-plugins-0.3)
Requires:	gnome-settings-daemon
Requires:	grilo
Requires:	python-dbus
Requires:	python-gi
Requires:	tracker
Requires: typelib(GIRepository)
Requires:	typelib(Grl)
Requires:	typelib(MediaArt)
Requires:	typelib(TotemPlParser)
Requires:	typelib(Tracker)
Requires: typelib(Goa)
Requires: typelib(Dazzle)

Requires: typelib(Atk)
Requires: typelib(GLib)
Requires: typelib(GModule)
Requires: typelib(GObject)
Requires: typelib(Gdk)
Requires: typelib(GdkPixbuf)
#Requires: typelib(Gfm)
Requires: typelib(Gio)
Requires: typelib(Gst)
Requires: typelib(GstPbutils)
Requires: typelib(GstTag)
Requires: typelib(Gtk)
Requires: typelib(Pango)
Requires: typelib(Soup)
Requires: typelib(cairo)
Requires: typelib(xlib)

Recommends:	grilo-plugins


%description
Music is the new GNOME music playing application.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

find %{buildroot} -name '*.la' -delete


%files -f %{name}.lang
%{_bindir}/%{name}
#{_libdir}/org.gnome.Music/
%{python3_sitelib}/gnomemusic
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/org.gnome.Music/
%{_iconsdir}/*/*/*/*
%{_datadir}/metainfo/org.gnome.Music.appdata.xml
%{_datadir}/locale/*/LC_MESSAGES/org.gnome.Music.mo

