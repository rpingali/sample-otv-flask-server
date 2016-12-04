from flask import Flask
from flask import request, url_for
import subprocess


def send_key(key):
	try:
		subprocess.call(
        	["irsend", "SIMULATE", "0000000000000476",    "-00", key, "DUMMYREMOTE"])
	except :
		print "error in sending key"
	return
	
app = Flask(__name__)



@app.route("/")
def hello():
    return "Hello World!"

@app.route("/remote/processKey")
def remote():
	key_value = request.args.get('key', 1)
	if key_value != None:
		send_key(key_value)
	return "remote pressed %s" % key_value


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

