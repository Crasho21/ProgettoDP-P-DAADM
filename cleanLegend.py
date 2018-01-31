import pymongo
from pymongo import MongoClient
from pprint import pprint
from pw import mongoPw

#Step 1: Connect to MongoDB and one DB
client = MongoClient('mongodb+srv://unige:' + mongoPw + '@cluster0-gf0ua.mongodb.net/test')
db = client.provadb
prova = db.prova

count = prova.count()
pprint(count)
for i in range(1, count):
    try:
        first = True
        name = prova.find_one({'id': i})['name']
        for p in prova.find({'name': name}).sort("id", pymongo.ASCENDING):
            if not first:
                #print("Record with id " + str(p['id']) + " deleted")
                prova.delete_one({'id': p['id']})
            first = False
    except Exception as err:
        print("Record with id " + str(i) + " not found")
        print(err)

count = prova.count()
pprint(count)
