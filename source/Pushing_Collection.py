import requests
import json

params = {'apiKey': 'vYIdoUBW4AwM6iSLEVwsx3BDsKxUCeis'}
url = 'https://api.mlab.com/api/1/databases'
response = requests.get(url, params)

print(response.status_code)
print(response.text)


dbname = 'lyricsdb'
collection = 'songs'
url = 'https://api.mlab.com/api/1/databases/' + dbname + '/collections/' + collection
headers = {'content-type': 'application/json'}
for i in range(len(collection)):
    data = json.dumps(collection[i])
    response = requests.post(url, data=data, params=params, headers=headers)