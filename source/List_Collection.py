import os
from bs4 import BeautifulSoup
import json
import requests

all=[]
all=list(os.listdir("lyrics_collection"))



collection=[]
for i in all[10:]:
    if i.endswith(".html"):
        f = open("lyrics_collection\my+place_20099978.html" ,'r')
        soup = BeautifulSoup(f, "lxml")
        link=soup.find("div", { "id" : "content_h" })
        lyr=(str(link)[31:-6].replace("<br/>", "\n"))
        link=soup.find("title")
        tit, art = str(link)[7:-8].split("-")
        dict={"artist": art.strip(), "title": tit.replace("Lyrics", "").strip(), "lyrics":lyr}
        collection.append(dict)


print(len(collection))

#pushing firsts documents
params = {'apiKey': 'vYIdoUBW4AwM6iSLEVwsx3BDsKxUCeis'}
url = 'https://api.mlab.com/api/1/databases'
response = requests.get(url, params)

print(response.status_code)
print(response.text)

dbname = 'lyricsdb'
collection = 'songs'
url = 'https://api.mlab.com/api/1/databases/' + dbname + '/collections/' + collection
headers = {'content-type': 'application/json'}

data = json.dumps(collection)
response = requests.post(url, data=data, params=params, headers=headers)

query = {"artist": "Celine Dion"}
params['q'] = json.dumps(query)
response = requests.get(url, params=params)
retrievedData = json.loads(response.text)
print(len(retrievedData))
print("fine")

