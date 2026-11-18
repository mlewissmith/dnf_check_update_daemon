## -*- meson -*-
message(meson.current_build_dir())

configure_file(
  input         : 'systemd.service.in',
  output        : PACKAGE + '.service',
  configuration : configx,
  install       : true,
  install_dir   : configx.get('systemd_unitdir'),
)
configure_file(
  input         : 'systemd.preset.in',
  output        : '95-' + PACKAGE + '.preset',
  configuration : configx,
  install       : true,
  install_dir   : configx.get('systemd_presetdir'),
)
