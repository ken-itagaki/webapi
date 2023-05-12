import requests

url = 'http://192.168.110.201/pandar.cgi?action=get&key=lidar_range'

responce = requests.get(url)

text = responce.json

print(text)