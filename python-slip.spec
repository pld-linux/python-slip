#
# Conditional build:
%bcond_without	python2	# CPython 2.x modules
%bcond_without	python3	# CPython 3.x modules
#
Summary:	Miscellaneous convenience, extension and workaround code for Python 2
Summary(pl.UTF-8):	Kod różnych udogodnień, rozszerzeń i obejść dla Pythona 2
Name:		python-slip
Version:	0.6.0
Release:	3
License:	GPL v2+
Group:		Development/Languages/Python
Source0:	https://fedorahosted.org/released/python-slip/%{name}-%{version}.tar.bz2
# Source0-md5:	fb3299d75af1a67ca6679d96ce839da6
URL:		https://fedorahosted.org/python-slip/
%if %{with python2}
BuildRequires:	python >= 2
BuildRequires:	python-devel >= 2
%endif
%if %{with python3}
BuildRequires:	python3 >= 3.2
BuildRequires:	python3-modules >= 3.2
%endif
BuildRequires:	rpmbuild(macros) >= 1.612
Requires:	python-selinux
Requires:	python-six
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Simple Library for Python packages contain miscellaneous code for
convenience, extension and workaround purposes.

This package provides the "slip" and the "slip.util" modules for
Python 2.

%description -l pl.UTF-8
Pakiety Simple Library for Python (prostej biblioteki dla Pythona)
zawierają kod różnych udogodnień, rozszerzeń i obejść.

Ten pakiet dostarcza moduły "slip" oraz "slip.util" dla Pythona 2.

%package dbus
Summary:	Convenience Python 2 functions for dbus services
Summary(pl.UTF-8):	Wygodne funkcje Pythona 2 dla usług dbus
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	python-dbus >= 0.80
Requires:	python-decorator
# pygobject2 or pygobject3 actually (using slip._wrapper._gobject)
Requires:	python-pygobject >= 2
Requires:	python-six
Suggests:	polkit >= 0.94
Conflicts:	PolicyKit < 0.8-3
Conflicts:	polkit < 0.94

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

%package -n python3-slip
Summary:	Miscellaneous convenience, extension and workaround code for Python 3
Summary(pl.UTF-8):	Kod różnych udogodnień, rozszerzeń i obejść dla Pythona 3
Group:		Development/Languages/Python
Requires:	python3-modules >= 3.2

%description -n python3-slip
The Simple Library for Python packages contain miscellaneous code for
convenience, extension and workaround purposes.

This package provides the "slip" and the "slip.util" modules for
Python 3.

%description -n python3-slip -l pl.UTF-8
Pakiety Simple Library for Python (prostej biblioteki dla Pythona)
zawierają kod różnych udogodnień, rozszerzeń i obejść.

Ten pakiet dostarcza moduły "slip" oraz "slip.util" dla Pythona 3.

%package -n python3-slip-dbus
Summary:	Convenience Python 3 functions for dbus services
Summary(pl.UTF-8):	Wygodne funkcje Pythona 3 dla usług dbus
Group:		Libraries
Requires:	python3-dbus >= 0.80
Requires:	python3-decorator
Requires:	python3-pygobject3 >= 3
Requires:	python3-six
Requires:	python3-slip = %{version}-%{release}
Suggests:	polkit >= 0.94
Conflicts:	PolicyKit < 0.8-3
Conflicts:	polkit < 0.94

%description -n python3-slip-dbus
The Simple Library for Python packages contain miscellaneous code for
convenience, extension and workaround purposes.

This package provides slip.dbus.service.Object, which is a
dbus.service.Object derivative that ends itself after a certain time
without being used and/or if there are no clients anymore on the
message bus, as well as convenience functions and decorators for
integrating a dbus service with PolicyKit.

%description -n python3-slip-dbus -l pl.UTF-8
Pakiety Simple Library for Python (prostej biblioteki dla Pythona)
zawierają kod różnych udogodnień, rozszerzeń i obejść.

Ten pakiet dostarcza slip.dbus.service.Object, będący pochodną
dbus.service.Object kończącą się po określonym czasie bezużyteczności
i/lub kiedy nie ma już klientów magistrali komunikatów, a także
wygodne funkcje i dekoratory służące integracji usług dbus z systemem
PolicyKit.

%prep
%setup -q

%build
%{__make} $(pwd)/setup.py

%if %{with python2}
%{__python} setup.py build \
	--build-base build-2
%endif

%if %{with python3}
%{__python3} setup.py build \
	--build-base build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%{__python} setup.py \
	build \
		--build-base build-2 \
	install \
		--optimize=2 \
		--root=$RPM_BUILD_ROOT \
		--skip-build

%py_postclean
%endif

%if %{with python3}
%{__python3} setup.py \
	build \
		--build-base build-3 \
	install \
		--optimize=2 \
		--root=$RPM_BUILD_ROOT \
		--skip-build
%endif

install -d $RPM_BUILD_ROOT%{_examplesdir}
cp -pr doc/dbus/example $RPM_BUILD_ROOT%{_examplesdir}/%{name}-dbus-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS
%dir %{py_sitescriptdir}/slip
%{py_sitescriptdir}/slip/__init__.py[co]
%{py_sitescriptdir}/slip/_wrappers
%{py_sitescriptdir}/slip/util
%{py_sitescriptdir}/slip-%{version}-py*.egg-info

%files dbus
%defattr(644,root,root,755)
%doc doc/dbus/README
%{py_sitescriptdir}/slip/dbus
%{py_sitescriptdir}/slip.dbus-%{version}-py*.egg-info
%{_examplesdir}/%{name}-dbus-%{version}

%files gtk
%defattr(644,root,root,755)
%{py_sitescriptdir}/slip/gtk
%{py_sitescriptdir}/slip.gtk-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-slip
%defattr(644,root,root,755)
%doc AUTHORS
%dir %{py3_sitescriptdir}/slip
%{py3_sitescriptdir}/slip/__init__.py
%{py3_sitescriptdir}/slip/__pycache__
%{py3_sitescriptdir}/slip/_wrappers
%{py3_sitescriptdir}/slip/util
%{py3_sitescriptdir}/slip-%{version}-py*.egg-info

%files -n python3-slip-dbus
%defattr(644,root,root,755)
%doc doc/dbus/README
%{py3_sitescriptdir}/slip/dbus
%{py3_sitescriptdir}/slip.dbus-%{version}-py*.egg-info
%endif
