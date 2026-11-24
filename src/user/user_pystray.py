import pystray
from PIL import Image
import threading
import subprocess

updates_txt="updates.txt"

icon_image = Image.new('RGB', (32,32), "cyan")

def __inotifywait():
    while True:
        subprocess.run(['inotifywait','-eclose_write',updates_txt])
        subprocess.run(['cat',updates_txt])

def menu_action_start(i,q):
    __inotifywait()

def menu_action(i, q):
    print(q)

def menu_action_stop(i,q):
    i.stop()

# default backend 'appindicator' does not support default action
# gtk backend supports default action (envvar PYSTRAY_BACKEND=gtk)
systray_icon = pystray.Icon(
    "NAME", icon_image, "TITLE",
    menu=pystray.Menu(
        pystray.MenuItem("start", menu_action_start),
        pystray.MenuItem("status", menu_action, default=True),
        pystray.MenuItem("settings", menu_action),
        pystray.MenuItem("stop", menu_action_stop),
    )
)


watch_thread = threading.Thread(target=__inotifywait, daemon=True)
watch_thread.start()
systray_icon.run()



### some ideas from
### https://stackoverflow.com/questions/66286498/can-should-i-use-asyncio-instead-of-threading-with-pystray
