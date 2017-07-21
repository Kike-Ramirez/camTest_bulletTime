import requests


r = requests.post("http://127.0.0.1:8000/stop")

print(r.text) # displays the result body.