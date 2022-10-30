Summary:	Managed D-Bus implementation - GLib integration
Name:		dbus-sharp-glib
Version:	0.6.0
Release:	1
License:	MIT
Group:		System/Libraries
Url:		http://mono.github.com/dbus-sharp/
Source0:	https://github.com/mono/dbus-sharp-glib/releases/download/v%(echo %{version}|cut -d. -f1-2)/dbus-sharp-glib-%{version}.tar.gz
BuildRequires:	gtk-sharp2
BuildRequires:	dbus-sharp-devel
BuildRequires:	pkgconfig(mono)
Requires:	glib2
BuildArch:	noarch

%description
dbus-sharp is a C# implementation of D-Bus. It's often referred to as
"managed D-Bus" to avoid confusion with existing bindings (which wrap
libdbus). This is the GLib integration for ndesk-dbus.

D-Bus is an inter-process communication framework that lets
applications interface with the system event bus as well as allowing
them to talk to one another in a peer-to-peer configuration.

%files
%doc README COPYING
%{_prefix}/lib/mono/%{name}-1.0
%{_prefix}/lib/mono/gac/%{name}/

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description devel
dbus-sharp is a C# implementation of D-Bus. It's often referred to as
"managed D-Bus" to avoid confusion with existing bindings (which wrap
libdbus). This is the GLib integration for ndesk-dbus.

D-Bus is an inter-process communication framework that lets
applications interface with the system event bus as well as allowing
them to talk to one another in a peer-to-peer configuration.

%files devel
%doc examples
%{_datadir}/pkgconfig/%{name}-1.0.pc

#----------------------------------------------------------------------------

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make

%install
%makeinstall_std pkgconfigdir=%{_datadir}/pkgconfig

