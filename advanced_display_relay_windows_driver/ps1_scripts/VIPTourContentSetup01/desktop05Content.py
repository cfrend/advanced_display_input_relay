92#! c:\api\automation\Scripts\python.exe
from pywinauto import application
import time
from win32api import GetSystemMetrics

#print("Width =", GetSystemMetrics(0))
#print("Height =", GetSystemMetrics(1))

screenWidth = GetSystemMetrics(0)
screenHeight = GetSystemMetrics(1)

def calcX(percentage):
    value = percentage * screenWidth
    return int(value)

def calcY(percentage):
    value = percentage * screenHeight
    return int(value)

try:
    app = application.Application(backend="win32")
    #app.start("Notepad.exe")
    app.start(r"C:\Program Files\ChimeraX\bin\ChimeraX.exe")
    time.sleep(7)
    dlg_spec = app.window()
    dlg_spec.move_window(x=calcX(0.5), y=calcY(0.5), width=calcX(0.51), height=calcY(0.51), repaint=True)
except:
    print("Could not launch ChimeraX properly, check on automation technique.")

try:
    app2 = application.Application()
    app2.start(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe /new-window --url https://sketchfab.com/3d-models/mathers-museum-teaching-collection-sc5548-e8319670a77847009eb9850c32636654 --force-renderer-accessibility")
    time.sleep(2)
    app2_sub = application.Application().connect(title = 'Mathers Museum Teaching Collection: SC5548 - 3D model by Indiana University - Advanced Visualization Lab (@AVL) [e831967] - Sketchfab - Google Chrome')
    app2_sub.window(title = 'Mathers Museum Teaching Collection: SC5548 - 3D model by Indiana University - Advanced Visualization Lab (@AVL) [e831967] - Sketchfab - Google Chrome').move_window(x=0, y=calcY(0.5), width=calcX(0.51), height=calcY(0.51), repaint=True)
except:
    print("Could not launch Mathers Model properly, check on automation technique.")

try:
    app3 = application.Application()
    app3.start(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe /new-window --url https://my.matterport.com/show/?m=oyUQ7bgzwHB --force-renderer-accessibility")
    time.sleep(2)
    app3_sub = application.Application().connect(title = 'Maxwell Hall - Google Chrome')
    app3_sub.window(title = 'Maxwell Hall - Google Chrome').move_window(x=0, y=0, width=calcX(1.0), height=calcY(0.51), repaint=True)
    time.sleep(1)
    send_keys('^r')
except:
    print("Could not launch Maxwell Hall Matterport properly, check on automation technique.")
