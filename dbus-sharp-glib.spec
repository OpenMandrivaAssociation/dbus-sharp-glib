%define pkgname %{name}-1.0

Summary:	Managed D-Bus implementation - GLib integration
Group:		System/Libraries
Name:		dbus-sharp-glib
Version:	0.5.0
Release:	3
License:	MIT
Url:		http://mono.github.com/dbus-sharp/
Source0:	http://github.com/downloads/mono/dbus-sharp/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	mono-devel
BuildRequires:	dbus-sharp-devel
BuildRequires:	gtk-sharp2
Requires:	glib2

%define _requires_exceptions lib.*glib2.0_0

%description
dbus-sharp is a C# implementation of D-Bus. It's often referred to as
"managed D-Bus" to avoid confusion with existing bindings (which wrap
libdbus). This is the GLib integration for ndesk-dbus.

D-Bus is an inter-process communication framework that lets
applications interface with the system event bus as well as allowing
them to talk to one another in a peer-to-peer configuration.

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

%description devel
dbus-sharp is a C# implementation of D-Bus. It's often referred to as
"managed D-Bus" to avoid confusion with existing bindings (which wrap
libdbus). This is the GLib integration for ndesk-dbus.

D-Bus is an inter-process communication framework that lets
applications interface with the system event bus as well as allowing
them to talk to one another in a peer-to-peer configuration.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
%make

%install
rm -rf %{buildroot}
%makeinstall_std pkgconfigdir=%{_datadir}/pkgconfig

%files
%doc README COPYING
%{_prefix}/lib/mono/%{pkgname}/
%{_prefix}/lib/mono/gac/%{name}/

%files devel
%doc examples
%{_datadir}/pkgconfig/%{pkgname}.pc
