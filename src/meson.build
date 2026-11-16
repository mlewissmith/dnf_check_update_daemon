## -*- meson -*-
fs = import('fs')
cbdpath = meson.current_build_dir()
cbdname = fs.name(cbdpath)
message('Entering ' + cbdpath)


configure_file(
  input         : 'daemon.sh.in',
  output        : 'daemon.sh',
  configuration : configx,
  install       : true,
  install_dir   : configx.get('pkglibexecdir'),
  install_mode  : 'rwx------',
)

configure_file(
  input         : 'systemd.service.in',
  output        : configx.get('PACKAGE_NAME') + '.service',
  configuration : configx,
  install       : false,
)
