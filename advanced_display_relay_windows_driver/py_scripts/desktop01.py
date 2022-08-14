#! c:\api\automation\Scripts\python.exe
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
    app.start(r"C:\Program Files\Google\Google Earth Pro\client\googleearth.exe")
    time.sleep(7)
    dlg_spec = app.window()
    dlg_spec.move_window(x=0, y=calcY(0.5), width=calcX(0.51), height=calcY(0.51), repaint=True)
except:
    print("Could not launch Google Earth properly, check on automation technique.")

try:
    app2 = application.Application()
    app2.start(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe /new-window --url https://skfb.ly/VQKC --force-renderer-accessibility")
    time.sleep(2)
    app2_sub = application.Application().connect(title = 'Barbers Bleeding Bowl - 3D model by Indiana University - Advanced Visualization Lab (@AVL) [da9ccb3] - Sketchfab - Google Chrome')
    app2_sub.window(title = 'Barbers Bleeding Bowl - 3D model by Indiana University - Advanced Visualization Lab (@AVL) [da9ccb3] - Sketchfab - Google Chrome').move_window(x=0, y=0, width=calcX(0.51), height=calcY(0.51), repaint=True)
except:
    print("Could not launch Bleeder Bowl properly, check on automation technique.")

try:
    app3 = application.Application()
    app3.start(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe /new-window --url https://showcase.avl.iu.edu/projects --force-renderer-accessibility")
    time.sleep(2)
    app3_sub = application.Application().connect(title = 'AVL Showcase - Google Chrome')
    app3_sub.window(title = 'AVL Showcase - Google Chrome').move_window(x=calcX(0.5), y=0, width=calcX(0.51), height=calcY(1.1), repaint=True)
except:
    print("Could not launch AVL Showcase properly, check on automation technique.")
