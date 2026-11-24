import pystray
from PIL import Image

icon_image = Image.new('RGB', (32,32), "cyan")

def menu_action(i, q):
    print(q)
    if str(q) == "stop":
        i.stop()

# default backend 'appindicator' does not support default action
# gtk backend supports default action (envvar PYSTRAY_BACKEND=gtk)
systray_icon = pystray.Icon(
    "NAME", icon_image, "TITLE",
    menu=pystray.Menu(
        pystray.MenuItem("start", menu_action),
        pystray.MenuItem("status", menu_action, default=True),
        pystray.MenuItem("settings", menu_action),
        pystray.MenuItem("stop", menu_action),
    )
)

systray_icon.run()
