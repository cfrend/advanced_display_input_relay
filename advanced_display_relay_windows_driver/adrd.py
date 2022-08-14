from utilities import Utility
from time import sleep
import requests
import json
import threading

#ADR Fields variables
adrAddress = "localhost"
adrURL = "http://" + adrAddress
adrUpEndpoint = "/is_up"
readAdrField_1 = "/adr_fields/read?adr_field=adr_field_1"
readAdrField_2 = "/adr_fields/read?adr_field=adr_field_2"
readAdrField_3 = "/adr_fields/read?adr_field=adr_field_3"


#Foot Pedal Input Variables
footPedalMode = ""

#Main thread super loop
while True:
    # Foot Pedal mode check
    modeUrl = adrURL + readAdrField_3
    rawModeData = 0
    try:
        rawModeData = requests.get(modeUrl, timeout=0.25)
    except requests.exceptions.RequestException as e:
        pass
    # This check is to help when adr server is down or booting up to help script not crash
    if (rawModeData != 0):
        if (rawModeData.status_code == 200):
            parsedModeFieldData = rawModeData.json()
            modeFieldData = json.loads(parsedModeFieldData['json_data'])
            # Check foot pedal mode
            if (modeFieldData['desktop change mode with animation'] == "ON"):
                footPedalMode = "desktop change mode with animation"
            if (modeFieldData['desktop change mode without animation'] == "ON"):
                footPedalMode = "desktop change mode without animation"
            if (modeFieldData['chrome tab change mode'] == "ON"):
                footPedalMode = "chrome tab change mode"
            if (modeFieldData['arrow mode'] == "ON"):
                footPedalMode = "arrow mode"
            if (modeFieldData['arrow mode'] == "OFF" and modeFieldData['chrome tab change mode'] == "OFF" and modeFieldData['desktop change mode without animation'] == "OFF" and modeFieldData['desktop change mode with animation'] == "OFF"):
                footPedalMode = ""
    

    # Foot Pedal input processing
    # Read & parse adr field data from the adr service
    url = adrURL + readAdrField_1
    rawData = 0
    try:
        rawData = requests.get(url, timeout=0.25)
    except requests.exceptions.RequestException as e:
        pass
    # This check is to help when adr server is down or booting up to help script not crash
    if (rawData != 0):
        if (rawData.status_code == 200):
            parsedFieldData = rawData.json()
            fieldData = json.loads(parsedFieldData['json_data'])

    # Changing Desktops with animation mode
    if (footPedalMode == 'desktop change mode with animation'):
        # Extracting prev/next desktop fields
        nextDesktop = fieldData['nextDesktop']
        Utility.nextDesktopAnimation(nextDesktop)
        prevDesktop = fieldData['prevDesktop']
        Utility.prevDesktopAnimation(prevDesktop)
        #print("NEXT "+nextDesktop)
        #print("PREV"+prevDesktop)

    # Changing Desktops without animation mode
    if (footPedalMode == 'desktop change mode without animation'):
        # Extracting prev/next desktop fields
        nextDesktop = fieldData['nextDesktop']
        Utility.nextDesktop(nextDesktop)
        prevDesktop = fieldData['prevDesktop']
        Utility.prevDesktop(prevDesktop)
        #print("NEXT "+nextDesktop)
        #print("PREV"+prevDesktop)

    # Changing Chrome Tab mode
    if (footPedalMode == 'chrome tab change mode'):
        # Extracting prev/next desktop fields
        nextDesktop = fieldData['nextDesktop']
        Utility.nextChromeTab(nextDesktop)
        prevDesktop = fieldData['prevDesktop']
        Utility.prevChromeTab(prevDesktop)
        #print("NEXT "+nextDesktop)
        #print("PREV"+prevDesktop)

    # Arrow mode
    if (footPedalMode == 'arrow mode'):
        # Extracting prev/next desktop fields
        nextDesktop = fieldData['nextDesktop']
        Utility.rightArrow(nextDesktop)
        prevDesktop = fieldData['prevDesktop']
        Utility.leftArrow(prevDesktop)
        #print("NEXT "+nextDesktop)
        #print("PREV"+prevDesktop)

    sleep(0.0083) #120Hz