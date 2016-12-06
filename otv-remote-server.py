from flask import Flask
from flask import request, url_for
import subprocess

test_appman = "/usr/local/bin/test_appman_proxy"


def send_key(key):
	try:
		key_str = "SIMLATE 0000000000000476   00  %s DUMMYREMOTE" % key
		print key_str
		subprocess.call(
        	["irsend", key_str])
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
	if key_value != None:
		if key_value == "GUIDE":
			launch_app("EdgeGravity-HTML", "NAGRA")

		send_key(key_value)
	return "remote pressed %s" % key_value


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
