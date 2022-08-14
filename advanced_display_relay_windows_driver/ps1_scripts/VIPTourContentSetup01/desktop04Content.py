#! c:\api\automation\Scripts\python.exe
from pywinauto import application
from pywinauto.keyboard import send_keys
import time

app = application.Application()

try:
    app.start(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe --url https://collectome.rt.iu.edu/frontend/exhibit-display/5f29cd481c2c1")
    time.sleep(5)
    dlg_spec = app.window()
    send_keys('{F11}')
    time.sleep(1)
    send_keys('^r')
except:
    print("Could not launch SciVis Collectome properly, check on automation technique.")

#app.start(r"C:\Program Files\Mozilla Firefox\firefox.exe --url https://collectome.rt.iu.edu/frontend/exhibit-display/5ec6c7595e5ae")
