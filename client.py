import requests
import http, subprocess

url = 'http://localhost:8088/users'
myobj = {'somekey':'somevalue'}

x = requests.post(url, data=myobj)
print(x.text)