#! c:\api\automation\Scripts\python.exe
from pywinauto import application
import time
from win32api import GetSystemMetrics

screenWidth = GetSystemMetrics(0)
screenHeight = GetSystemMetrics(1)

def calcX(percentage):
    value = percentage * screenWidth
    return int(value)

def calcY(percentage):
    value = percentage * screenHeight
    return int(value)

app = application.Application()
app.start(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe /new-window --url https://poly.google.com/view/1shaZxghkas --force-renderer-accessibility")
#print(app['Name'])
time.sleep(2)
#print(app.dump_tree())
app_sub = application.Application().connect(title = 'IU Campus Limestone Tour - Poly - Google Chrome')
app_sub.window(title = 'IU Campus Limestone Tour - Poly - Google Chrome').move_window(x=0, y=0, width=calcX(0.5), height=calcY(0.5), repaint=True)
#print(type(app_sub))
#dlg_spec = app.window(title = 'IU Campus Limestone Tour - Poly - Google Chrome')
#dlg_spec.move_window(x=0, y=0, width=calcX(0.5), height=calcY(0.5), repaint=True)
