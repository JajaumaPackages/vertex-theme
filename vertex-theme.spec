Name:           vertex-theme
Version:        20160329
Release:        1%{?dist}
Summary:        A theme for GTK 3, GTK 2, Gnome-Shell and Cinnamon

License:        GPLv3.0
URL:            https://github.com/horst3180/vertex-theme
Source0:        https://github.com/horst3180/vertex-theme/archive/%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gtk3-devel
Requires:       gnome-themes-standard
Requires:       gtk-murrine-engine

%description
Vertex is a theme for GTK 3, GTK 2, Gnome-Shell and Cinnamon. It supports GTK 3
and GTK 2 based desktop environments like Gnome, Cinnamon, Mate, XFCE, Budgie,
Pantheon, etc. Themes for the Browsers Chrome/Chromium and Firefox are
included, too.


%prep
%setup -q
./autogen.sh


%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install


%files
%doc AUTHORS README.md
%license COPYING
%{_datadir}/themes/Vertex/
%{_datadir}/themes/Vertex-Dark/
%{_datadir}/themes/Vertex-Light/


%changelog
* Wed Sep 28 2016 Jajauma's Packages <jajauma@yandex.ru> - 20160329-1
- Public release
