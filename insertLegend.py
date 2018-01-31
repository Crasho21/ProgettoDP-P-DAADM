import pymongo
from pprint import pprint
from pw import mongoPw

#Step 1: Connect to MongoDB and one DB
client = MongoClient('mongodb+srv://unige:' + mongoPw + '@cluster0-gf0ua.mongodb.net/test')
db = client.provadb

#Step 2: Create a collection into the DB
prova = db.prova
#Creating unique attribute id
result = db.prova.create_index([('id', pymongo.ASCENDING)], unique = True)
legend = open("DatiUCI/legend.txt","r")
id = 0
while 1:
    line = legend.readline()
    if len(line) == 0:
        break
    temp = line.split(" ")
    id = int(temp[0])
    flag = temp[1]
    s = temp[2]
    temp2 = s.split("->")
    name = temp2[0]
    #print(str(id) + " " + flag + " " + name)
    #Catching error for duplicate entries
    try:
        #Step 3: Create a document
        p = {   "id": id,
                "flag": flag,
                "name": name,
            }
        #Step 4: Insert a document
        sample_id = prova.insert_one(p).inserted_id
    except:
        print("Value with id = " + str(id) + " already inserted!")
legend.close()
count = prova.find().count()
pprint(count)
