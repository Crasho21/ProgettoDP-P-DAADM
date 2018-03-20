import pymongo
from pymongo import MongoClient
from pprint import pprint
from pw import mongoPw

#Step 1: Connect to MongoDB and one DB
client = MongoClient('mongodb+srv://unige:' + mongoPw + '@cluster0-gf0ua.mongodb.net/test')
db = client.provadb

#Step 2: Create a collection into the DB
legend = db.legend
conversionData = open("DatiUCI/conversionTable.txt","r")
conversionTable = []
while 1:
    line = conversionData.readline()
    if len(line) == 0:
        break
    conversionTable.append(int(line))
#print(conversionTable)
print(len(conversionTable))
conversionData.close()
print("Done!")
