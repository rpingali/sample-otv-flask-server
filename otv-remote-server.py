from flask import Flask
from flask import request, url_for
import subprocess

test_appman = "/usr/local/bin/test_appman_proxy"


def send_key(key):
	try:
		key_str = "0000000000000476   00  %s DUMMYREMOTE" % key
		print key_str
		subprocess.call(
        	["irsend", "SIMULATE", key_str])
	except :
		print "error in sending key"
	return

def request_state(appId,prodId, state):
    subprocess.call(
              [test_appman, "-c", "requestAppState", "-a", appId, "-p", prodId, "-s" , str(state)  ])
    return

def launch_app(appId, prodId):
	request_state(appId, prodId, 1)
	return

app = Flask(__name__)



@app.route("/")
def hello():
    return "Hello World!"

@app.route("/remote/processKey")
def remote():

	key_value = request.args.get('key', 1)
	key_value = key_value.upper()
	if key_value != None:
		if key_value == "GUIDE":
			launch_app("EdgeGravity-HTML", "NAGRA")

		send_key(key_value)
	return "remote pressed %s" % key_value


#/CCOM/ApplicationManager/requestAppState?state=1&appId=YouTube&prodId=NAGRA
@app.route("/CCOM/ApplicationManager/requestAppState")
def appman_ccom():
	state = request.args.get('state', 1)
	appId = request.args.get('appId', 1)
	prodId = request.args.get('prodId', 1)
#	print (appId , prodId, state)
	request_state(appId, prodId , state)
	return "OK"



if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
