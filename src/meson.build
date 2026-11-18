## -*- meson -*-
message(meson.current_build_dir())

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
endif

if get_option('with-profile_d')
  subdir('profile_d')
endif
