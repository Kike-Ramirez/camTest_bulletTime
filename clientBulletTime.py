import requests
import wget
import time

r = requests.post("http://10.42.0.255:8000/start")

time.sleep(4)

r = requests.post("http://10.42.0.255:8000/stop")
 



for i in range (26,27):

	time.sleep(0.2)
	print 'Pidiendo foto: ' + str(i)
	file_url = 'http://10.42.0.' + str(100 + i) + ':8000/get/10'

	try:
		file_name = wget.download(file_url)
		file_name.save('/Finals/' + str(i) + '_picture.png')

	except:
		print "File not received"