import time
from SimpleCV import Camera
from flask import Flask, request


app = Flask(__name__)

@app.route('/start', methods=['POST'])
def result():
    print(request.form['foo']) # should display 'bar'
    return 'Start !' # response to your request.


app.run(host= 'localhost', port= '8000')

cam = Camera()
time.sleep(0.1)  # If you don't wait, the image will be dark
num = 0
continueFlag = True

while continueFlag:

	try:
		nameFile = str(num) + "_picture.png"
		img = cam.getImage()
		img.save(nameFile)
		num += 1
		time.sleep(0.1)
		print 'Tomada foto: ' + str(num)

	except KeyboardInterrupt:

		print 'Saliendo...'
		continueFlag = False

