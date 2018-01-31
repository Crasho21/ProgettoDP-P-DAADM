import pymongo
from pprint import pprint
from pw import mongoPw

#Step 1: Connect to MongoDB and one DB
client = MongoClient('mongodb+srv://unige:' + mongoPw + '@cluster0-gf0ua.mongodb.net/test')
#Drop a db
#client.drop_database('provadb')
db = client.provadb

#Step 2: Create a collection into the DB
prova = db.prova
#Creating unique attribute id
result = db.prova.create_index([('id', pymongo.ASCENDING)], unique = True)
#prova.delete_many({'type':"1"})

for i in range (1, 5):
    #Catching error for duplicate entries
    try:
        #Step 3: Create a document
        p = {   "id": i,
                "type": 1,
                "tags": ["1", "22", "54"],
            }
        #Step 4: Insert a document
        post_id = prova.insert_one(p).inserted_id
        break
    except:
        print("Value with id = " + str(i) + " already inserted!")

#Step 5: Find one document and count
#pprint(posts.find_one())
pprint(prova.find_one({'id': 1}))
pprint(prova.find_one({'id': 2}))
pprint(prova.find_one({'id': 3}))
pprint(prova.find_one({'id': 4}))
count = prova.find({'type': 1}).count()
pprint(count)
count = prova.find({'id': 1}).count()
pprint(count)
