#! c:\api\automation\Scripts\python.exe
from pywinauto import application
from pywinauto.keyboard import send_keys
import time

send_keys('{VK_CONTROL down}{VK_LSHIFT down}')
send_keys('{VK_TAB}')
time.sleep(0.1)
send_keys('{VK_CONTROL up}{VK_LSHIFT up}')