Name:          zramcfg
Version:       0.0.6
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
mkdir -p %{buildoot}/etc/default

cp -p zramcfg.sh %{buildroot}/usr/bin/zramcfg
cp -p zramcfg-jolla %{buildroot}/etc/default/zramcfg

### FILES
%files
%defattr(-,root,root,-)
%{_sysconfdir}
%{_bindir}

### POST AND POSTUN (depmod)
%post -p /usr/bin/zramcfg
%preun -p /usr/bin/zramcfg -r
