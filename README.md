zramcfg
=======

zramcfg is a really simple, bash-written configuration tool for the zRAM
kernel module.

Unlike zram-config (ubuntu) and the one used in elementary OS (along with other scripts based on these), zramcfg
does not provide an {init,upstart,systemd} script that gets executed at boot.  
Instead, it uses udev and the modprobe configuration directories to create the zram devices.

The usage is simple: put the configuration file "zramcfg" in /etc/default/, then use

    sudo zramcfg

to enable zram, or

    sudo zramcfg -r

to disable it.

See the configuration file if you want to tweak the devices number and the size of them.
