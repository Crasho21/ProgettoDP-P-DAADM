import pymongo
from pymongo import MongoClient
from pprint import pprint
import threading
from pw import mongoPw

# Thread for creating part of the conversion table
def createConvTable(lb, ub):
    print("Thread started\n")
    outputData = open("DatiUCI/conversionTable " + str(lb) + "-" + str(ub) + ".txt", "w")
    try:
        #conversionTable = []
        for i in range(lb, ub + 1):
            n = legend.find_one({'id': i})['name']
            temp = legend.find({'name': n}).sort("id", pymongo.ASCENDING)
            temp = next(temp)['id']
            #conversionTable.append(temp)
            outputData.write(str(temp) + "\n")
            #if i % 5000 == 0:
                #print(i)
    except Exception as err:
        print(err)
    #print(conversionTable)
    outputData.close()
    print("From " + str(lb) + " to " + str(ub) + " done!")

# Connect to MongoDB and one DB
client = MongoClient('mongodb+srv://unige:' + mongoPw + '@cluster0-gf0ua.mongodb.net/test')
db = client.provadb

print("Creating conversion table...\n" +  time.strftime("%d/%m/%Y %H:%M:%S", time.localtime()) + "\n")
legend = db.legend

# Launching threads
threads = []
for i in range(0, 325000, 5000):
    thread = threading.Thread(target = createConvTable, args = (i + 1, i + 5000))
    thread.start()
    threads.append(thread)
thread = threading.Thread(target = createConvTable, args = (325001, 326110))
thread.start()
threads.append(thread)

# Waiting threads to finish
for t in threads:
    t.join()

# Copying all parts of the conversion table into 1 file
outputData = open("DatiUCI/conversionTable.txt","w")
for i in range(0, 325000, 5000):
    inputData = open("DatiUCI/conversionTable " + str(i + 1) + "-" + str(i + 5000) + ".txt", "r")
    while 1:
        line = inputData.readline()
        if len(line) == 0:
            break
        outputData.write(line)
    inputData.close()
inputData = open("DatiUCI/conversionTable 325001-326110.txt", "r")
while 1:
    line = inputData.readline()
    if len(line) == 0:
        break
    outputData.write(line)
inputData.close()
outputData.close()
print("Conversion table created!" +  time.strftime("%d/%m/%Y %H:%M:%S", time.localtime()) + "\n")
