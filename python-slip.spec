Summary:	Miscellaneous convenience, extension and workaround code for Python
Summary(pl.UTF-8):	Kod różnych udogodnień, rozszerzeń i obejść dla Pythona
Name:		python-slip
Version:	0.2.20
Release:	3
License:	GPL v2+
Group:		Development/Languages/Python
Source0:	https://fedorahosted.org/released/python-slip/%{name}-%{version}.tar.bz2
# Source0-md5:	4e0267cbeb2cb1666c5930bd7c7acfb4
URL:		https://fedorahosted.org/python-slip/
BuildRequires:	python >= 2
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	python-devel >= 2
Requires:	python-selinux
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Simple Library for Python packages contain miscellaneous code for
convenience, extension and workaround purposes.

This package provides the "slip" and the "slip.util" modules.

%description -l pl.UTF-8
Pakiety Simple Library for Python (prostej biblioteki dla Pythona)
zawierają kod różnych udogodnień, rozszerzeń i obejść.

Ten pakiet dostarcza moduły "slip" oraz "slip.util".

%package dbus
Summary:	Convenience functions for dbus services
Summary(pl.UTF-8):	Wygodne funkcje dla usług dbus
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	polkit >= 0.94
Requires:	python-dbus >= 0.80
Requires:	python-decorator
Requires:	python-pygobject >= 2
Conflicts:	PolicyKit < 0.8-3

%description dbus
The Simple Library for Python packages contain miscellaneous code for
convenience, extension and workaround purposes.

This package provides slip.dbus.service.Object, which is a
dbus.service.Object derivative that ends itself after a certain time
without being used and/or if there are no clients anymore on the
message bus, as well as convenience functions and decorators for
integrating a dbus service with PolicyKit.

%description dbus -l pl.UTF-8
Pakiety Simple Library for Python (prostej biblioteki dla Pythona)
zawierają kod różnych udogodnień, rozszerzeń i obejść.

Ten pakiet dostarcza slip.dbus.service.Object, będący pochodną
dbus.service.Object kończącą się po określonym czasie bezużyteczności
i/lub kiedy nie ma już klientów magistrali komunikatów, a także
wygodne funkcje i dekoratory służące integracji usług dbus z systemem
PolicyKit.

%package gtk
Summary:	Code to make auto-wrapping GTK+ labels
Summary(pl.UTF-8):	Kod do tworzenia automatycznie zawijanych etykiet GTK+
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	python-pygtk-gtk >= 2:2

%description gtk
The Simple Library for Python packages contain miscellaneous code for
convenience, extension and workaround purposes.

This package provides slip.gtk.set_autowrap(), a convenience function
which lets GTK+ labels be automatically re-wrapped upon resizing.

%description gtk -l pl.UTF-8
Pakiety Simple Library for Python (prostej biblioteki dla Pythona)
zawierają kod różnych udogodnień, rozszerzeń i obejść.

Ten pakiet dostarcza slip.gtk.set_autowrap() - wygodną funkcję
pozwalającą na automatyczne zawijanie etykiet GTK+ przy zmianie
rozmiaru.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}
cp -pr doc/dbus/example $RPM_BUILD_ROOT%{_examplesdir}/%{name}-dbus-%{version}

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%dir %{py_sitescriptdir}/slip
%{py_sitescriptdir}/slip/__init__.py[co]
%{py_sitescriptdir}/slip/util
%{py_sitescriptdir}/slip-%{version}-py%{python_version}.egg-info

%files dbus
%defattr(644,root,root,755)
%doc doc/dbus/README
%{py_sitescriptdir}/slip/dbus
%{py_sitescriptdir}/slip.dbus-%{version}-py%{python_version}.egg-info
%{_examplesdir}/%{name}-dbus-%{version}

%files gtk
%defattr(644,root,root,755)
%{py_sitescriptdir}/slip/gtk
%{py_sitescriptdir}/slip.gtk-%{version}-py%{python_version}.egg-info
