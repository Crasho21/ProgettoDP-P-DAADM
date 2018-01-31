import pymongo
from pymongo import MongoClient
from pprint import pprint
from pw import mongoPw

#Step 1: Connect to MongoDB and one DB
client = MongoClient('mongodb+srv://unige:' + mongoPw + '@cluster0-gf0ua.mongodb.net/test')
db = client.provadb

#Step 2: Create a collection into the DB
db.data.delete_many({})
data = db.data
prova = db.prova
#Creating unique attribute id
#result = data.create_index([('id', pymongo.ASCENDING)], unique = True)
inputData = open("DatiUCI/data.txt","r")
id = 0
while id < 10:
    line = inputData.readline()
    if len(line) == 0:
        break
    id = id + 1
    flag = int(line[0])
    s = line[2 : ]
    name = s.split(" ")
    name = name[0 : -1]
    #print(str(id) + " " + str(flag) + " " + str(name))
    #Catching error for duplicate entries
    try:
        temp2 = []
        for i in range(0, len(name)):
            n = prova.find_one({'id': int(name[i])})['name']
            temp = prova.find({'name': n}).sort("id", pymongo.ASCENDING)
            temp = next(temp)['id']
            temp2.append(temp)
            temp2 = list(set(map(int, temp2)))
        name = sorted(temp2)
        #name = list(set(name))
        #Step 3: Create a document
        p = {   "id": id,
                "flag": flag,
                "name": name,
            }
        #print(p)
        #Step 4: Insert a document
        sample_id = data.insert_one(p).inserted_id
    except Exception as err:
        #print("Value with id = " + str(id) + " already inserted!")
        print(err)
inputData.close()
count = data.count()
pprint(count)
