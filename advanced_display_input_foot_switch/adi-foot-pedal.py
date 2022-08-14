from time import sleep
import RPi.GPIO as GPIO
import requests
import urllib.parse
from socket import *
import socket
import os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

nextBtn = 5
prevBtn = 27

GPIO.setup(nextBtn, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(prevBtn, GPIO.IN, pull_up_down = GPIO.PUD_UP)

lastNextBtnState = "OFF"
lastPrevBtnState = "OFF"

class InputCommunications:
    # ADR service connection variables
    ipaddr = ''
    adrAddress = "<ip address for ADR server>"
    adrURL = "http://" + adrAddress
    adrUpEndpoint = "/is_up"
    # Foot Pedal input variables for communications
    writeAdrField_1 = "/adr_fields/new?adr_field=adr_field_1&json_data="
    bothOff = '{"nextDesktop":"OFF","prevDesktop":"OFF"}'
    nextOn = '{"nextDesktop":"ON","prevDesktop":"OFF"}'
    prevOn = '{"nextDesktop":"OFF","prevDesktop":"ON"}'
    lastURL = adrURL + writeAdrField_1 + urllib.parse.quote(bothOff)
    # Foot Pedal connection variables for communications
    writeAdrField_2 = "/adr_fields/new?adr_field=adr_field_2&json_data="
    connectionJsonPrefix = '{"foot pedal ip address":"'
    connectionJsonSufix = '"}'

    def reportConnection():
        payload = InputCommunications.connectionJsonPrefix + InputCommunications.ipaddr + InputCommunications.connectionJsonSufix
        urlEncodedPayload = urllib.parse.quote(payload)
        url = InputCommunications.adrURL + InputCommunications.writeAdrField_2 + urlEncodedPayload
        #print ("REPORTING FOOT PEDAL URL WITH ", url)
        InputCommunications.sendConnectionReport(url)
    
    def sendConnectionReport(url_with_payload):
        try:
            response = requests.get(url_with_payload, timeout=0.1)
        except requests.exceptions.RequestException as e:
            pass

    def checkForConnection():
        #Interrogate the current connection
        gw = os.popen("ip -4 route show default").read().split()
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        if len(gw) > 0:
                s.connect((gw[2], 0))
                InputCommunications.ipaddr = s.getsockname()[0]
                #Report IP address of foot pedal to ADR
                InputCommunications.reportConnection()
        else:
                InputCommunications.ipaddr = '127.0.0.1'
        print("IP ADDRESS FOUND AS ", InputCommunications.ipaddr)

    def sendInput(json_data):
        url = InputCommunications.adrURL + InputCommunications.writeAdrField_1
        urlEncodedPayload = urllib.parse.quote(json_data)
        url = url + urlEncodedPayload
        # Only send if the URL is constructed correctly
        urlCheck = url.split('/')
        if (urlCheck[0] == 'http:'):
            # Only send if it's a differnt URL
            if (InputCommunications.lastURL != url):
                try:
                    response = requests.get(url, timeout=0.1)
                except requests.exceptions.RequestException as e:
                    pass
                print(json_data)
        InputCommunications.lastURL = url
    
# Input system super loop thread
while True:

    # Check for an active web connection
    if (InputCommunications.ipaddr == '127.0.0.1' or InputCommunications.ipaddr == ''):
        InputCommunications.checkForConnection()
    # If the web is connected run the super loop
    else:
        # Collect button states
        nextBtnState = GPIO.input(nextBtn)
        # Process Next on button press not state
        if (nextBtnState == 1 and lastNextBtnState == "OFF"):
            # Trigger next
            InputCommunications.sendInput(InputCommunications.nextOn)
        if (nextBtnState == 0 and lastNextBtnState == "ON"):
            # Trigger next
            InputCommunications.sendInput(InputCommunications.nextOn)        

        prevBtnState = GPIO.input(prevBtn)
        # Process Prev on button press not state
        if (prevBtnState == 1 and lastPrevBtnState == "OFF"):
            # Trigger prev
            InputCommunications.sendInput(InputCommunications.prevOn)
        if (prevBtnState == 0 and lastPrevBtnState == "ON"):
            # Trigger prev
            InputCommunications.sendInput(InputCommunications.prevOn)

            # Process off state for next & prev when they don't change
        if ((nextBtnState == 1 and lastNextBtnState == "ON") and (prevBtnState == 1 and lastPrevBtnState == "ON")):
            # Trigger both off
            InputCommunications.sendInput(InputCommunications.bothOff)
        if ((nextBtnState == 0 and lastNextBtnState == "OFF") and (prevBtnState == 0 and lastPrevBtnState == "OFF")):
            # Trigger both off
            InputCommunications.sendInput(InputCommunications.bothOff)
        if ((nextBtnState == 0 and lastNextBtnState == "OFF") and (prevBtnState == 1 and lastPrevBtnState == "ON")):
            # Trigger both off
            InputCommunications.sendInput(InputCommunications.bothOff)
        if ((nextBtnState == 1 and lastNextBtnState == "ON") and (prevBtnState == 0 and lastPrevBtnState == "OFF")):
            # Trigger both off
            InputCommunications.sendInput(InputCommunications.bothOff)

        # Set last states
        # Next Button
        if (nextBtnState == 1):
            lastNextBtnState = "ON"
        if (nextBtnState == 0):
            lastNextBtnState = "OFF"
        # Prev Button
        if (prevBtnState == 1):
            lastPrevBtnState = "ON"
        if (prevBtnState == 0):
            lastPrevBtnState = "OFF"
        #print("NEXT "+str(nextBtnState))
        #print("PREV "+str(prevBtnState))
    sleep(0.033) #30 Hz

