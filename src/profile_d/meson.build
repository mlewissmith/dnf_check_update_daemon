## -*- meson -*-
message(meson.current_build_dir())

configure_file(
  input         : 'profile_d.bash.in',
  output        : PACKAGE + '.sh',
  configuration : configx,
  install       : true,
  install_dir   : configx.get('sysconfdir')/'profile.d',
)
