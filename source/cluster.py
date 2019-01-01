from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
from collections import Counter
#from pymongo import MongoClient
#from bson.son import SON
#from sklearn.cluster import KMeans
#from scipy.cluster.hierarchy import dendrogram, linkage
import json
#import plotly.plotly as py
#import plotly.figure_factory as ff
#from wordcloud import WordCloud
#import matplotlib.pyplot as plt
ps = PorterStemmer()
from math import log


with open('lyrics.json', 'r', encoding='utf-8') as json_data:
    lyrics = json.load(json_data)
    json_data.close()
    
with open('vocabulary.json', 'r', encoding='utf-8') as json_data:
    vocabulary = json.load(json_data)
    json_data.close()

with open('index.json', 'r', encoding='utf-8') as json_data:
    index = json.load(json_data)
    json_data.close()

with open('frequency.json', 'r', encoding='utf-8') as json_data:
    frequency = json.load(json_data)
    json_data.close()


q=input("enter the set:").split()
query=list(map(lambda x: ps.stem(x), q))



'''
params = {'apiKey': 'RKnHYU5eIIdsSC6h5nhwm2zck7FYFgTp'}
dbname = 'lyricsdb'
collection = 'Index'
url = 'https://api.mlab.com/api/1/databases/' + dbname + '/collections/' + collection
headers = {'content-type': 'application/json'}


db = MongoClient("mongodb://lyrics:123456789@ds113936.mlab.com:13936/lyricsdb").lyricsdb

pipeline = [
    {"$unwind": "$lyrics"},
    {"$limit": 10},
    {"$group": {"_id": "$lyrics"}},
    {"$sort": SON([("count", -1), ("_id", -1)])}]

a=list(db.songs.aggregate(pipeline))
'''
songs={}

for key, values in lyrics.items():
    if all(words in values for words in query):          
        songs[key]=values


list1=songs.keys()
list2=index[]
 

'''
a=[]
words={}
for j in songs.values():
    a.append(j)
    for z in j:
        words[i]=log(len(songs)/))

#set of document we are interested in
for i in a:
    words+=i
words=set(words)


'''
'''
idf = {}
      
for i in songs.values():
    document+=1
    freq=Counter(e)
    frequency[document]=freq
    for j in i:
        if j not in idf:
            idf[j]= 0


kmeans = KMeans(n_clusters=5, init='random')
#dendrogram(kmeans, orientation="right", labels=names)
print(kmeans)
dendrogram(kmeans)

#wordcloud = WordCloud(max_font_size=40).generate(kmeans)
'''