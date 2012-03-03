# TODO
# - fix bashism: sh: >&/dev/null : illegal file descriptor name
Summary:	Miscellaneous convenience, extension and workaround code for Python
Name:		python-slip
Version:	0.2.20
Release:	2.3
License:	GPL v2+
Group:		Development/Languages/Python
URL:		http://fedorahosted.org/python-slip
Source0:	http://fedorahosted.org/released/python-slip/%{name}-%{version}.tar.bz2
# Source0-md5:	4e0267cbeb2cb1666c5930bd7c7acfb4
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	python-devel
Requires:	python-selinux
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Simple Library for Python packages contain miscellaneous code for
convenience, extension and workaround purposes.

This package provides the "slip" and the "slip.util" modules.

%package dbus
Summary:	Convenience functions for dbus services
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	polkit >= 0.94
Requires:	python-dbus >= 0.80
Requires:	python-decorator
Requires:	python-pygobject
Conflicts:	PolicyKit < 0.8-3

%description dbus
The Simple Library for Python packages contain miscellaneous code for
convenience, extension and workaround purposes.

This package provides slip.dbus.service.Object, which is a
dbus.service.Object derivative that ends itself after a certain time
without being used and/or if there are no clients anymore on the
message bus, as well as convenience functions and decorators for
integrating a dbus service with PolicyKit.

%package gtk
Summary:	Code to make auto-wrapping gtk labels
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	python-pygtk-gtk

%description gtk
The Simple Library for Python packages contain miscellaneous code for
convenience, extension and workaround purposes.

This package provides slip.gtk.set_autowrap(), a convenience function
which lets Gtk labels be automatically re-wrapped upon resizing.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING doc/dbus
%dir %{py_sitescriptdir}/slip
%{py_sitescriptdir}/slip/__init__.py[co]
%{py_sitescriptdir}/slip/util
%{py_sitescriptdir}/slip-%{version}-py%{python_version}.egg-info

%files dbus
%defattr(644,root,root,755)
%doc doc/dbus/*
%{py_sitescriptdir}/slip/dbus
%{py_sitescriptdir}/slip.dbus-%{version}-py%{python_version}.egg-info

%files gtk
%defattr(644,root,root,755)
%{py_sitescriptdir}/slip/gtk
%{py_sitescriptdir}/slip.gtk-%{version}-py%{python_version}.egg-info
