import time
# from SimpleCV import Camera
import threading
from threading import Thread
from flask import Flask


app = Flask(__name__)

# cam = Camera()
time.sleep(0.1)  # If you don't wait, the image will be dark
num = 0
continueFlag = True


@app.route('/start', methods=['POST'])
def start():
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
		nameFile = str(num) + "_picture.png"
		# img = cam.getImage()
		# img.save(nameFile)
		num += 1
		print 'Tomada foto: ' + str(num)




if __name__ == '__main__':
	try:
		run_event = threading.Event()
		run_event.set()
		threadCamera = Thread(target = t_getFrames)
		threadCamera.daemon = True
		threadCamera.start()

		app.run(host= '127.0.0.1', port= '8000')

	except KeyboardInterrupt, SystemExit:
		continueFlag = False
		run_event.clear()
		thread.join(0)
