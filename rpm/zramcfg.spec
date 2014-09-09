Name:          zramcfg
Version:       0.0.8
Summary:       configuration tool for the zRAM kernel module
Release:       1
License:       GPLv3+
Group:         System Environment/Kernel

Source0:       zramcfg-%{version}.tar.bz2

Requires:      bash
Requires:      kernel-module-zram-jolla
Requires:      gawk
Requires:      grep
Requires:      sed
Requires:      systemd

BuildArch:     noarch

%description
zramcfg is a really simple, bash-written configuration tool
for the zRAM kernel module.

Unlike zram-config (ubuntu) and the one used in elementary OS
(along with other scripts based on these), zramcfg does not provide
an {init,upstart,systemd} script that gets executed at boot.  
Instead, it uses udev and the modprobe configuration directories
to create the zram devices.

### PREP
%prep
%setup -q -c

### BUILD
%build


### INSTALL
%install
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/etc/default
#mkdir -p %{buildroot}/lib/systemd/system

cp -p zramcfg.sh %{buildroot}/usr/bin/zramcfg
cp -p zramcfg-fallback %{buildroot}/usr/bin/zramcfg-fallback
cp -p zramcfg-jolla %{buildroot}/etc/default/zramcfg
#cp -p service/zramcfg-fallback.service %{buildroot}/lib/systemd/system

chmod +x %{buildroot}/usr/bin/zramcfg*

### FILES
%files
%defattr(-,root,root,-)
%{_sysconfdir}
%{_bindir}
#/lib/systemd/system

### POST AND PREUN
%post
#systemctl enable zramcfg-fallback.service
zramcfg

%preun
#systemctl disable zramcfg-fallback.service
zramcfg -r
