import requests
import wget
import time

r = requests.post("http://10.42.0.255:8000/start")

time.sleep(4)

r = requests.post("http://10.42.0.255:8000/stop")
 



file_url = 'http://10.42.0.100/get/10'

try:
	file_name = wget.download(file_url)
	file_name.save(/'pictures/10_picture.png')

except:
	print "File not received"