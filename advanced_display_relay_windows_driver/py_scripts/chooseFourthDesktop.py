#! c:\api\automation\Scripts\python.exe
from pywinauto import application
from pywinauto import mouse
from pywinauto.keyboard import send_keys
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

send_keys('{LWIN down}{TAB down}')
time.sleep(0.25)
send_keys('{LWIN up}{TAB up}')
time.sleep(0.25)
mouse.click(button='left',coords=(calcX(0.22), calcY(0.05)))
