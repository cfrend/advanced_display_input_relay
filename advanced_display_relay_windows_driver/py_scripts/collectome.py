#! c:\api\automation\Scripts\python.exe
from pywinauto import application
from pywinauto.keyboard import send_keys
import time

app = application.Application()
#app.start(r"C:\Program Files\Mozilla Firefox\firefox.exe --url https://collectome.rt.iu.edu/frontend/exhibit-display/5ec6c7595e5ae")
app.start(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe --url https://collectome.rt.iu.edu/frontend/exhibit-display/5ec6c7595e5ae")
time.sleep(3)
dlg_spec = app.window()
send_keys('{F11}')
time.sleep(1)
send_keys('^r')
