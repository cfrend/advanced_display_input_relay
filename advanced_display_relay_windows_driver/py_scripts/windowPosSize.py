#! c:\api\automation\Scripts\python.exe
from pywinauto import application
import time

app = application.Application()
#app.start("Notepad.exe")
app.start("C:\Program Files\Google\Google Earth Pro\client\googleearth.exe")
time.sleep(5)
dlg_spec = app.window()
dlg_spec.move_window(x=0, y=500, width=400, height=300, repaint=True)
