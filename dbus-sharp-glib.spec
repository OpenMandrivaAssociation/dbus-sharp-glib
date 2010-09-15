%define name dbus-sharp-glib
%define version 0.5.0
%define release %mkrel 1
%define pkgname %name-1.0

Summary: Managed D-Bus implementation - GLib integration
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://github.com/downloads/mono/dbus-sharp/%{name}-%{version}.tar.gz
License: MIT
Group: System/Libraries
Url: http://mono.github.com/dbus-sharp/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mono-devel
BuildRequires: dbus-sharp-devel
BuildRequires: gtk-sharp2
Requires: glib2
BuildArch: noarch
%define _requires_exceptions lib.*glib2.0_0

%description
dbus-sharp is a C# implementation of D-Bus. It's often referred to as
"managed D-Bus" to avoid confusion with existing bindings (which wrap
libdbus). This is the GLib integration for ndesk-dbus.

D-Bus is an inter-process communication framework that lets
applications interface with the system event bus as well as allowing
them to talk to one another in a peer-to-peer configuration.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
dbus-sharp is a C# implementation of D-Bus. It's often referred to as
"managed D-Bus" to avoid confusion with existing bindings (which wrap
libdbus). This is the GLib integration for ndesk-dbus.

D-Bus is an inter-process communication framework that lets
applications interface with the system event bus as well as allowing
them to talk to one another in a peer-to-peer configuration.

%prep
%setup -q -n %name-%version

%build
./configure --prefix=%_prefix
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std pkgconfigdir=%_datadir/pkgconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README COPYING
%_prefix/lib/mono/%pkgname
%_prefix/lib/mono/gac/%name/

%files devel
%defattr(-,root,root)
%doc examples
%_datadir/pkgconfig/%pkgname.pc