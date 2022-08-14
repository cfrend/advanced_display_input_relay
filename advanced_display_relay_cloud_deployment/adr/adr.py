from flask import Flask, render_template, request, make_response
import requests
from flask_cors import CORS
from views.adr_fields import adr_field_blueprint, read_internal
import qrcode
import json

app = Flask(__name__, static_folder="/var/www/adr/static", template_folder="/var/www/adr/templates")
app.config.from_object('config')

class server_internals:
    server_addr = ""

    #Function to generate new QR code image for /QR endpoint page
    def refreshQR(addressToUse):
        qr = qrcode.QRCode(
            version=5,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        #qrPayload = 'http://' + addressToUse +'/'
        qr.add_data(addressToUse)
        qr.make()

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(r'/var/www/adr/static/qr-code.png')

# CRUD for general I/O syning with avl string objects
app.register_blueprint(adr_field_blueprint, url_prefix="/adr_fields")

@app.route('/is_up', methods=['GET'])
def hello_world():
    # Just a debug endpoint
    return render_template('up.html')

@app.route('/foot-pedal', methods=['GET'])
def foot():
    # Collect server address from adr field for use below
    addr = ""
    try:
        addr = read_internal('adr_field_0')
    except:
        pass
    if (addr != ""):
        # parse out IP address
        obj = addr['json_data']
        #return render_template('test.html', obj=obj)
        objDict = json.loads(obj)
        server_internals.server_addr = objDict['adr ip address']
    # Configure foot pedal input modes
    return render_template('foot-pedal.html', server_addr=server_internals.server_addr)

@app.route('/qr-foot-pedal', methods=['GET'])
def qrfoot():
    # Collect server address from adr field for use below
    addr = ""
    try:
        addr = read_internal('adr_field_0')
    except:
        pass
    if (addr != ""):
        # parse out IP address
        obj = addr['json_data']
        #return render_template('test.html', obj=obj)
        objDict = json.loads(obj)
        server_internals.server_addr = objDict['adr ip address']
    
    if (server_internals.server_addr != ""):
        addressToUse = 'http://' + server_internals.server_addr + '/foot-pedal'
        server_internals.refreshQR(addressToUse)
        # Link page for foot pedal input modes page
        return render_template('qr-foot-pedal.html', server_addr=server_internals.server_addr)
    if (server_internals.server_addr == ""):
        # Initialization error page
        return render_template('initialize-error.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000, threaded=True)# ssl_context="adhoc", threaded=True)