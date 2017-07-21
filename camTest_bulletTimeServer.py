import time
from SimpleCV import Camera
import threading
from threading import Thread
from flask import Flask
from flask import send_file
import shutil
from os import listdir
from os.path import isfile, join
import json
from pprint import pprint

data = []

with open('settings.json') as data_file:    
    
    data = json.load(data_file)



app = Flask(__name__)

cam = Camera()
time.sleep(0.5)  # If you don't wait, the image will be dark
num = 0


@app.route('/start', methods=['POST'])
def start():

	shutil.rmtree('/pictures')
	os.makedirs(directory)
	run_event.set()
	print 'Start'
	t_getFrames()
	return 'Received Start'


@app.route('/stop', methods=['POST'])
def stop():
	run_event.clear()
	print 'Stop'
	return 'Received Stop'

def t_getFrames():
	global num
	while run_event.is_set():
		time.sleep(0.002)
		nameFile = "/pictures/" + str(num) + "_picture.png"
		img = cam.getImage()
		img.save(nameFile)
		num += 1
		print 'Tomada foto: ' + str(num)


@app.route('/get/<number>', methods=['POST'])
def getFrameNum( number ):

	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

	tempFileObj = NamedTemporaryFile(mode='w+b',suffix='png')

	for file in onlyfiles:

		print file
		if file == str(num) + '_picture.png':
	   		response = send_file(tempFileObj, as_attachment=True, attachment_filename=file)
	   		print 'File sent'
    		return response



if __name__ == '__main__':
	try:
		run_event = threading.Event()
		#run_event.set()
		threadCamera = Thread(target = t_getFrames)
		threadCamera.daemon = True
		threadCamera.start()

		url = '10.42.0.' + str(int(data["cam"]["id"]) + 100)

		app.run(host= url, port= '8000')

	except KeyboardInterrupt, SystemExit:
		continueFlag = False
		run_event.clear()
		thread.join(0)
