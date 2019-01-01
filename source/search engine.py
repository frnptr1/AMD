from nltk.stem import PorterStemmer
ps = PorterStemmer()
import json
from math import *
from nltk.stem import PorterStemmer
ps=PorterStemmer()
import numpy as np
from _heapq import *

with open('vocabulary.json', 'r', encoding='utf-8') as json_data:
    vocabulary = json.load(json_data)
    json_data.close()

with open('lyrics.json', 'r', encoding='utf-8') as json_data:
    lyrics = json.load(json_data)
    json_data.close()

with open('index.json', 'r', encoding='utf-8') as json_data:
    index = json.load(json_data)
    json_data.close()

with open('frequency.json', 'r', encoding='utf-8') as json_data:
    frequency = json.load(json_data)
    json_data.close()


# defining heapsort to sort the heap structure
def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]

# intersection
def intersect(a, b):
    return list(set(a) & set(b))




# setting the query
a = input("enter the set:").split()
query = list(map(lambda x: ps.stem(x), a))


# retrieving the id of the query to find it inside the inverted index
ind = [vocabulary[i] for i in query]
'''

# norm of query
normq = sqrt(len(query))

# we will use N in the idf values
N = len(frequency)

# idf calculated for each word
idf = {}
for j in index.keys():
    idf[j] = log(N/len(index[j]))

# set of document we are interested in
a = []
d = []
for j in ind:
    # a contains now the list of the words retrieved by keys, i want to get a unique list with all the
    # unique(without repetition) documents
    a.append(index[str(j)].keys())
for i in a:
    d += i
d = set(d)

# this list will host the tf-idf cosine values
h = []
# this dict will contain the tf-idf cosine values linked to the n. of document which refears
final_dic = {}
for i in d:
    doc = []
    q = []
    # norm of document
    normd = []
    f = (frequency[str(i)])
    for key, values in f.items():
        normd.append(values*idf[str(vocabulary[key])])
    normdoc = np.linalg.norm(normd)

    for wd in query:
        try:
            doc.append(frequency[str(i)][wd]*(idf[str(vocabulary[wd])]))
            q.append(1)
        except KeyError:
            doc.append(0)
            q.append(0)
    # numerator
    numerator=(np.dot(q,doc))
    # cosine
    cos=numerator/(normq*float(normdoc))
    final_dic[cos] = i
    h.append(cos)

# sorting the list with heapsort and getting back the 10 greatest values
a = heapsort(h)
nv = a[-10:]

# getting back the number of documents according to the cosine values and the dictonary final_dic
for i in nv:
    print(final_dic[i])
'''

songs = {}

for key, values in lyrics.items():
    if all(words in values for words in query):
        songs[key] = values



#creating the set of words we are interested in to build the tf-idf vector
a = []
words = []
for j in songs.values():
    a.append(j)
for i in a:
    words += i
words = set(words)

#creating the words idf dictonary (key: id of word - value: idf of word)
list1 = songs.keys()
list2=[]
wordsind = [vocabulary[i] for i in words]
wordsidf={}
for i in wordsind:
    list2=index[str(i)].keys()
    wordsidf[i]=(log(len(songs)/len(intersect(list1, list2))))



for key, values in songs.items():
    vector = []
    for wrd in values:
        tf=frequency[str(key)][wrd]
        idf=wordsidf[vocabulary[wrd]]
        vector.append(tf*idf)
    print(key, vector)

