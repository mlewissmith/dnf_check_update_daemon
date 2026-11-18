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

if get_option('with-systemd')
  subdir('systemd')
  # configure_file(
  #   input         : 'systemd.service.in',
  #   output        : configx.get('PACKAGE_NAME') + '.service',
  #   configuration : configx,
  #   install       : true,
  #   install_dir   : configx.get('systemd_unitdir'),
  # )
  # configure_file(
  #   input         : 'systemd.preset.in',
  #   output        : '95-' + configx.get('PACKAGE_NAME') + '.preset',
  #   configuration : configx,
  #   install       : true,
  #   install_dir   : configx.get('systemd_presetdir'),
  # )
endif

if get_option('with-profile_d')
  subdir('profile.d')
  # configure_file(
  #   input         : 'profile.bash.in',
  #   output        : configx.get('PACKAGE_NAME')+'.sh',
  #   configuration : configx,
  #   install       : true,
  #   install_dir   : configx.get('sysconfdir')/'profile.d',
  # )
endif
