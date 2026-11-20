## -*- meson -*-
message(meson.current_build_dir())

configure_file(
  input         : 'dcud.sh.in',
  output        : 'dcud.sh',
  configuration : configx,
  install       : true,
  install_dir   : configx.get('bindir'),
)
