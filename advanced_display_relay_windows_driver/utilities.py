#! c:\adrd\automation\Scripts\python.exe
import os

POWERSHELL_PATH = "C:\Windows\System32\WindowsPowerShell\\v1.0\powershell.exe"
PYTON_PATH = "python "
collectome_script_path = PYTON_PATH + r"C:\adrd\py_scripts\collectome.py"
vip_tour_content_01_setup_path = r"C:\adrd\ps1_scripts\VIPTourContentSetup01\VIPTourContentSetup.ps1"
animated_next_desktop = PYTON_PATH + r"C:\adrd\py_scripts\desktopRight.py"
animated_prev_desktop = PYTON_PATH + r"C:\adrd\py_scripts\desktopLeft.py"
next_chrome_tab = PYTON_PATH + r"C:\adrd\py_scripts\nextChromeTab.py"
prev_chrome_tab = PYTON_PATH + r"C:\adrd\py_scripts\prevChromeTab.py"
right_arrow = PYTON_PATH + r"C:\adrd\py_scripts\rightArrow.py"
left_arrow = PYTON_PATH + r"C:\adrd\py_scripts\leftArrow.py"
close_all_script_path = r"C:\adrd\ps1_scripts\close_all.ps1"
minimize_script_path = r"C:\adrd\ps1_scripts\minimizeall.ps1"
unminimize_script_path = r"C:\adrd\ps1_scripts\unminimizeall.ps1"
startup_script_path = PYTON_PATH + r"C:\adrd\py_scripts\startup.py"
desktop01_script_path = r"C:\adrd\ps1_scripts\switchToDesktop01.ps1"
desktop02_script_path = r"C:\adrd\ps1_scripts\switchToDesktop02.ps1"
desktop03_script_path = r"C:\adrd\ps1_scripts\switchToDesktop03.ps1"
desktop04_script_path = r"C:\adrd\ps1_scripts\switchToDesktop04.ps1"
desktop05_script_path = r"C:\adrd\ps1_scripts\switchToDesktop05.ps1"
trackpad_path = PYTON_PATH + r"C:\adrd\automation\static\virtualTrackpad\trackpad.py"

class Utility:  # SHARED CLASS TO USE IN OUR PROJECT
    # Previous variable states for onEvent type comparison behaviors
    lastNextDesktopState = "OFF"
    lastPrevDesktopState = "OFF"
    desktopState = 1

    def simple_ps_command(script_path):

        process_result =  os.system(POWERSHELL_PATH + " " + script_path)
        print(POWERSHELL_PATH + " " + script_path)
        return "done"

    def nextDesktopAnimation(newState):
        newState = newState.upper()
        if (newState == "ON" and Utility.lastNextDesktopState == "OFF"):
            os.system(animated_next_desktop)
            print("SCRIPT PATH USED " + animated_next_desktop)

        Utility.lastNextDesktopState = newState

    def prevDesktopAnimation(newState):
        newState = newState.upper()
        if (newState == "ON" and Utility.lastPrevDesktopState == "OFF"):
            os.system(animated_prev_desktop)
            print("SCRIPT PATH USED " + animated_prev_desktop)

        Utility.lastPrevDesktopState = newState

    def nextDesktop(newState):
        newState = newState.upper()
        if (newState == "ON" and Utility.lastNextDesktopState == "OFF"):
            Utility.simple_ps_command(Utility.nextDesktopState())

        Utility.lastNextDesktopState = newState

    def prevDesktop(newState):
        newState = newState.upper()
        if (newState == "ON" and Utility.lastPrevDesktopState == "OFF"):
            Utility.simple_ps_command(Utility.prevDesktopState())

        Utility.lastPrevDesktopState = newState

    def nextChromeTab(newState):
        newState = newState.upper()
        if (newState == "ON" and Utility.lastNextDesktopState == "OFF"):
            os.system(next_chrome_tab)
            print("SCRIPT PATH USED " + next_chrome_tab)

        Utility.lastNextDesktopState = newState

    def prevChromeTab(newState):
        newState = newState.upper()
        if (newState == "ON" and Utility.lastNextDesktopState == "OFF"):
            os.system(prev_chrome_tab)
            print("SCRIPT PATH USED " + prev_chrome_tab)

        Utility.lastNextDesktopState = newState

    def rightArrow(newState):
        newState = newState.upper()
        if (newState == "ON" and Utility.lastNextDesktopState == "OFF"):
            os.system(right_arrow)
            print("SCRIPT PATH USED " + right_arrow)

        Utility.lastNextDesktopState = newState

    def leftArrow(newState):
        newState = newState.upper()
        if (newState == "ON" and Utility.lastNextDesktopState == "OFF"):
            os.system(left_arrow)
            print("SCRIPT PATH USED " + left_arrow)

        Utility.lastNextDesktopState = newState

    # Used by nextDesktop()
    def nextDesktopState():
        if (Utility.desktopState == 1):
            Utility.desktopState = 2
            return desktop02_script_path

        if (Utility.desktopState == 2):
            Utility.desktopState = 3
            return desktop03_script_path

        if (Utility.desktopState == 3):
            Utility.desktopState = 4
            return desktop04_script_path

        if (Utility.desktopState == 4):
            Utility.desktopState = 5
            return desktop05_script_path

        if (Utility.desktopState == 5):
            Utility.desktopState = 1
            return desktop01_script_path

    # Used by prevDesktop()
    def prevDesktopState():
        if (Utility.desktopState == 1):
            Utility.desktopState = 5
            return desktop05_script_path

        if (Utility.desktopState == 2):
            Utility.desktopState = 1
            return desktop01_script_path

        if (Utility.desktopState == 3):
            Utility.desktopState = 2
            return desktop02_script_path

        if (Utility.desktopState == 4):
            Utility.desktopState = 3
            return desktop03_script_path

        if (Utility.desktopState == 5):
            Utility.desktopState = 4
            return desktop04_script_path

