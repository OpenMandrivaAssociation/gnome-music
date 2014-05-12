%define url_ver %(echo %{version}|cut -d. -f1,2)
%define _exclude_files_from_autoprov %{_libdir}/%{name}

Name:		gnome-music
Version:	3.12.1
Release:	%mkrel 1
Summary:	Music player and management application
License:	GPLv2+
Group:		Sound/Players
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

%find_lang %{name} --with-help

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


%changelog
* Mon Apr 14 2014 ovitters <ovitters> 3.12.1-1.mga5
+ Revision: 613974
- new version 3.12.1

* Mon Mar 24 2014 ovitters <ovitters> 3.12.0-1.mga5
+ Revision: 607975
- new version 3.12.0

* Mon Mar 17 2014 ovitters <ovitters> 3.11.92-1.mga5
+ Revision: 604414
- new version 3.11.92

* Wed Mar 05 2014 ovitters <ovitters> 3.11.91-1.mga5
+ Revision: 600234
- new version 3.11.91

* Mon Feb 17 2014 ovitters <ovitters> 3.11.90-1.mga5
+ Revision: 593854
- new version 3.11.90

* Wed Feb 05 2014 ovitters <ovitters> 3.11.2-1.mga5
+ Revision: 583245
- new version 3.11.2

* Tue Jan 07 2014 pterjan <pterjan> 3.10.1-4.mga4
+ Revision: 565456
- Add some missing dependencies (mga#11967)

* Sat Nov 09 2013 ovitters <ovitters> 3.10.1-3.mga4
+ Revision: 550163
- fix url

  + fwang <fwang>
    - drop filter

* Tue Oct 22 2013 umeabot <umeabot> 3.10.1-2.mga4
+ Revision: 542162
- Mageia 4 Mass Rebuild

* Mon Oct 14 2013 ovitters <ovitters> 3.10.1-1.mga4
+ Revision: 497032
- new version 3.10.1

* Mon Sep 23 2013 ovitters <ovitters> 3.10.0-1.mga4
+ Revision: 484031
- new version 3.10.0

  + pterjan <pterjan>
    - Remove duplicate lines in %%files

* Mon Sep 16 2013 ovitters <ovitters> 3.9.92-1.mga4
+ Revision: 480354
- new version 3.9.92

* Mon Sep 02 2013 ovitters <ovitters> 3.9.91-1.mga4
+ Revision: 474484
- new version 3.9.91

* Tue Aug 20 2013 fwang <fwang> 3.9.90-2.mga4
+ Revision: 468055
- tweak requires so that it won't confllicts with gnome-documents

* Tue Aug 20 2013 fwang <fwang> 3.9.90-1.mga4
+ Revision: 468047
- update file list
- imported package gnome-music

