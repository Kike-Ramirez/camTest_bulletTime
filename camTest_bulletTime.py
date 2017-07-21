import time
from SimpleCV import Camera


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

