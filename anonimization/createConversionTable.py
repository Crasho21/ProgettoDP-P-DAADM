import pymongo
from pymongo import MongoClient
from pprint import pprint
from pw import mongoPw

#Step 1: Connect to MongoDB and one DB
client = MongoClient('mongodb+srv://unige:' + mongoPw + '@cluster0-gf0ua.mongodb.net/test')
db = client.provadb

print("Creating conversion table...")
legend = db.legend
outputData = open("DatiUCI/conversionTable.txt","w")
try:
    #conversionTable = []
    for i in range(10001, 50000):
        n = legend.find_one({'id': i})['name']
        temp = legend.find({'name': n}).sort("id", pymongo.ASCENDING)
        temp = next(temp)['id']
        #conversionTable.append(temp)
        outputData.write(str(temp) + "\n")
        if i % 5000 == 0:
            print(i)
except Exception as err:
    print(err)
#print(conversionTable)
outputData.close()
print("Done!")
