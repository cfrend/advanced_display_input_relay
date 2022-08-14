#! c:\api\automation\Scripts\python.exe
from pywinauto import application
import time
from win32api import GetSystemMetrics
from pywinauto.keyboard import send_keys

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
    app = application.Application()
    app.start(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe /new-window --url https://my.matterport.com/show/?m=pMoJU6Qkgef --force-renderer-accessibility")
    time.sleep(2)
    app_sub = application.Application().connect(title = 'Kelley School of Business (Aug 2020) - Google Chrome')
    app_sub.window(title = 'Kelley School of Business (Aug 2020) - Google Chrome').move_window(x=0, y=0, width=calcX(1.0), height=calcY(1.0), repaint=True)
except:
    print("Could not launch Kelley School Matterport properly, check on automation technique.")

send_keys('{F11}')
time.sleep(1)
send_keys('^r')
