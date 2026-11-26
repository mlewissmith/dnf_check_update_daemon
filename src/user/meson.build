## -*- meson -*-
message(meson.current_build_dir())

configure_file(
  input         : 'dcud.sh.in',
  output        : 'dcud.sh',
  configuration : configx,
  install       : true,
  install_dir   : configx.get('bindir'),
  install_mode  : 'rwxr-xr-x',
  install_tag   : 'user',
)


configure_file(
  input         : 'user_notifyd.sh.in',
  output        : 'user_notifyd.sh',
  configuration : configx,
  install       : true,
  install_dir   : configx.get('pkglibexecdir'),
  install_mode  : 'rwxr-xr-x',
  install_tag   : 'user',
)

configure_file(
  input         : 'user_pystray.py.in',
  output        : 'user_pystray.py',
  configuration : configx,
  install       : true,
  install_dir   : configx.get('pkglibexecdir'),
  install_mode  : 'rwxr-xr-x',
  install_tag   : 'user',
)

