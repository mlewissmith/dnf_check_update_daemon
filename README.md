# dnf_notify_update
Notify users of available packages updates


+ `/var/lib/rpm/rpmdb.sqlite` is database of installed packages;
  updates on `dnf install ...`
+ `/var/cache/dnf/packages.db` is database of available packages;
  updates on `dnf makecache`
