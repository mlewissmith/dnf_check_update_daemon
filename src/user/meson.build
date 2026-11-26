## -*- meson -*-
message(meson.current_build_dir())

fs = import('fs')

configx_user = configuration_data()
configx_user.merge_from(configx)
configx_user.set('__dcud_sh',          configx_user.get('bindir')/'dcud.sh')
configx_user.set('__user_notifyd_sh',  configx_user.get('pkglibexecdir')/'user_notifyd.sh')
configx_user.set('__user_pystray_py',  configx_user.get('pkglibexecdir')/'user_pystray.py')
configx_user.set('_dcud_desktop',      configx_user.get('datadir')/'applications'/'dcud.desktop')


summary(
  {
    '__dcud_sh'         : configx_user.get('__dcud_sh'),
    '__user_notifyd_sh' : configx_user.get('__user_notifyd_sh'),
    '__user_pystray_py' : configx_user.get('__user_pystray_py'),
    '_dcud_desktop'     : configx_user.get('_dcud_desktop'),
  },
  section: 'configx_user',
)

configure_file(
  input         : 'dcud.sh.in',
  output        : fs.name(configx_user.get('__dcud_sh')),
  configuration : configx_user,
  install       : true,
  install_dir   : fs.parent(configx_user.get('__dcud_sh')),
  install_mode  : 'rwxr-xr-x',
  install_tag   : 'user',
)

configure_file(
  input         : 'user_notifyd.sh.in',
  output        : fs.name(configx_user.get('__user_notifyd_sh')),
  configuration : configx_user,
  install       : true,
  install_dir   : fs.parent(configx_user.get('__user_notifyd_sh')),
  install_mode  : 'rwxr-xr-x',
  install_tag   : 'user',
)

configure_file(
  input         : 'user_pystray.py.in',
  output        : fs.name(configx_user.get('__user_pystray_py')),
  configuration : configx_user,
  install       : true,
  install_dir   : fs.parent(configx_user.get('__user_pystray_py')),
  install_mode  : 'rwxr-xr-x',
  install_tag   : 'user',
)

configure_file(
  input         : 'dcud.desktop.in',
  output        : fs.name(configx_user.get('_dcud_desktop')),
  configuration : configx_user,
  install       : true,
  install_dir   : fs.parent(configx_user.get('_dcud_desktop')),
  install_mode  : 'rw-r--r--',
  install_tag   : 'user',
)
