# Only the portals.conf files are packaged. Upstream retired the Vala portal
# backend after this Baseline (regolith-linux/xdg-desktop-portal-regolith#39),
# and the Baseline's configuration never routes to it, so it is not built and
# there is no xdg-desktop-portal-regolith package: Fedora has no older backend
# to replace.

Name:           xdg-desktop-portal-regolith
Version:        0.3.11
Release:        1%{?dist}
Summary:        Regolith configuration for xdg-desktop-portal
# COPYING is the GPL version 3 text and no file names another licence;
# debian/copyright says Apache-2.0.
License:        GPL-3.0-only
URL:            https://github.com/regolith-linux/xdg-desktop-portal-regolith
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description
Configuration files that tell xdg-desktop-portal which portal backends to use
in the Regolith sessions.

%package        wayland-config
Summary:        Regolith Wayland session configuration for xdg-desktop-portal
# portals.conf files with [preferred] need xdg-desktop-portal 1.17 or later;
# Debian asks for 1.20. The backends it names (wlr, gtk, gnome-keyring) come
# with the session.
Requires:       xdg-desktop-portal >= 1.20

%description    wayland-config
Selects the portal backends for the Regolith Wayland session
(XDG_CURRENT_DESKTOP Regolith-Wayland): the backend for sway first, then GTK,
with GNOME Keyring for secrets, and turns off the portals that have no backend
there.

%package        x11-config
Summary:        Regolith X11 session configuration for xdg-desktop-portal
Requires:       xdg-desktop-portal >= 1.20

%description    x11-config
Selects the portal backends for the Regolith X11 session (XDG_CURRENT_DESKTOP
Regolith): GTK, with GNOME Keyring for secrets, and turns off the portals that
have no backend there.

%prep
%autosetup

%build

%install
install -Dpm 0644 data/regolith-wayland-portals.conf %{buildroot}%{_datadir}/xdg-desktop-portal/regolith-wayland-portals.conf
install -Dpm 0644 data/regolith-portals.conf %{buildroot}%{_datadir}/xdg-desktop-portal/regolith-portals.conf

%files wayland-config
%license COPYING
%{_datadir}/xdg-desktop-portal/regolith-wayland-portals.conf

%files x11-config
%license COPYING
%{_datadir}/xdg-desktop-portal/regolith-portals.conf

%changelog
* Mon Nov 16 2026 Regolith Fedora Port <port@regolith.invalid> - 0.3.11-1
- Initial package: the portals.conf files only
