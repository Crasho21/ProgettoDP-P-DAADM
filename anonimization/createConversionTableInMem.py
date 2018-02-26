import pymongo
from pymongo import MongoClient
from pprint import pprint
from pw import mongoPw
import time

#Step 1: Connect to MongoDB and one DB
# client = MongoClient('mongodb+srv://unige:' + mongoPw + '@cluster0-gf0ua.mongodb.net/test')
# db = client.provadb

print("Creating conversion table... " + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime()) )
# legend = db.legend
outputData = open("DatiUCI/conversionTable.txt","w")

#read legend
inputLegend = open("DatiUCI/legend.txt","r")
inputArr = []
while True:
    line = inputLegend.readline()
    if len(line) == 0:
        break
    temp = line.split(" ")
    id = int(temp[0])
    flag = temp[1]
    s = temp[2]
    temp2 = s.split("->")
    name = temp2[0]
    inputArr.append(name)

print("End loading legend.txt")

try:
    #conversionTable = []
    for i in range(0, len(inputArr)):
        # n = legend.find_one({'id': i})['name']
        n = inputArr[i]
        # temp = legend.find({'name': n}).sort("id", pymongo.ASCENDING)
        temp = inputArr.index(n)+1
        # temp = next(temp)['id']
        #conversionTable.append(temp)
        outputData.write(str(temp) + "\n")
        if i % 5000 == 0:
            print(i)
except Exception as err:
    print(err)

#print(conversionTable)
outputData.close()
print("Done!" +  time.strftime("%d/%m/%Y %H:%M:%S", time.localtime()))
