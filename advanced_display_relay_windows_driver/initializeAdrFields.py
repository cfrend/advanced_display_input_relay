import requests
import socket
import urllib.parse
from time import sleep
from pywinauto import application

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

#Construct payload to send to ADR field 0 for use on k8s pod flask endpoints
systemIP = get_ip()
adr_field_0_prefix = '{"adr ip address":"'
adr_field_0_suffix = '"}'
adr_field_0_payload = adr_field_0_prefix + systemIP + adr_field_0_suffix
adr_field_0_payload = urllib.parse.quote(adr_field_0_payload)

adr_field_0_init = "http://localhost/adr_fields/new?adr_field=adr_field_0&json_data="
adr_field_0_init = adr_field_0_init + adr_field_0_payload
adr_field_1_init = "http://localhost/adr_fields/new?adr_field=adr_field_1&json_data=%7B%22nextDesktop%22%3A%22OFF%22%2C%22prevDesktop%22%3A%22OFF%22%7D"
adr_field_3_init = "http://localhost/adr_fields/new?adr_field=adr_field_3&json_data=%7B%22desktop%20change%20mode%20without%20animation%22%3A%22OFF%22%2C%22desktop%20change%20mode%20with%20animation%22%3A%22ON%22%2C%22chrome%20tab%20change%20mode%22%3A%22OFF%22%2C%22arrow%20mode%22%3A%22OFF%22%7D"

while True:
    initResponse0 = ""
    initResponse1 = ""
    initResponse3 = ""
    try:
        initResponse0 = requests.get(adr_field_0_init, timeout=0.25)
        initResponse1 = requests.get(adr_field_1_init, timeout=0.25)
        initResponse3 = requests.get(adr_field_3_init, timeout=0.25)
    except requests.exceptions.RequestException as e:
        pass
    if (initResponse0 != ""):
        print("ADR has been initialized")
        break
    sleep(0.033)

#Launch /qr-foot-pedal endpoint
try:
    app = application.Application()
    app.start(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe /new-window --url http://localhost/qr-foot-pedal --force-renderer-accessibility")
    
except:
    print("Could not launch /qr-foot-pedal page")