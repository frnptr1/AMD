from textblob import TextBlob as tb
from nltk.stem import PorterStemmer
ps = PorterStemmer()
import itertools
import json
from math import log
from nltk.stem import PorterStemmer
ps=PorterStemmer()
import numpy as np
from math import sqrt
from heapq import *

with open('vocabulary.json', 'r', encoding='utf-8') as json_data:
    vocabulary = json.load(json_data)
    json_data.close()

with open('index.json', 'r', encoding='utf-8') as json_data:
    index = json.load(json_data)
    json_data.close()

with open('frequency.json', 'r', encoding='utf-8') as json_data:
    frequency = json.load(json_data)
    json_data.close()

N=len(frequency)

#w=everything sun love great fun likely ok
a=input("enter the set:").split()
query=list(map(lambda x: ps.stem(x), a))
ind = [vocabulary[i] for i in query]


idf={}
for j in index.keys():
    idf[j]=log(N/len(index[j]))


a=[]
for j in ind:
    a.append(index[str(j)].keys())

#set of document we are interested in
d=[]
for i in a:
    d+=i
d=set(d)

#norm of query
normq=sqrt(len(query))

new_list = []
new_dict = {}
another = []
for i in d:
    doc=[]
    q=[]
    #norm of document
    normd=[]
    f=(frequency[str(i)])
    for key, values in f.items():
        normd.append(values*idf[str(vocabulary[key])])
    normdoc=np.linalg.norm(normd)

    for wd in query:
        try:
            doc.append(frequency[str(i)][wd]*(idf[str(vocabulary[wd])]))
            q.append(1)
        except KeyError:
            doc.append(0)
            q.append(0)
    #numerator
    numerator=(np.dot(q,doc))
    #cosine
    cos=numerator/(normq*float(normdoc))
    #print(cos)
    new_dict[cos] = i
    new_list.append(cos)

#print(new_dict)
#print(new_list)

def heapsort(iterable):

   h = []
   for value in iterable:
       heappush(h, value)
   return [heappop(h) for i in range(len(h))]


a = heapsort(new_list)
nv   =  a[-10:]

for i in nv:
    j = str(i)
    print(new_dict[i])













