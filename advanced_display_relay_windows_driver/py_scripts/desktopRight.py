#! c:\api\automation\Scripts\python.exe
from pywinauto import application
from pywinauto.keyboard import send_keys
import time

send_keys('{LWIN down}{VK_CONTROL down}')
send_keys('{RIGHT}')
time.sleep(0.1)
send_keys('{LWIN up}{VK_CONTROL up}')
