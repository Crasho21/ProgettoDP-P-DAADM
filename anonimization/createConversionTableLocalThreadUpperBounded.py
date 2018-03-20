import pymongo
from pymongo import MongoClient
from pprint import pprint
import threading
import time

# Function for searching id knowing name
def searchId(name):
    for i in range(0, len(legend)):
        if legend[i].split(" ")[2].strip('\n') == name:
            return i + 1

# Thread for creating part of the conversion table
def createConvTable(lb, ub):
    print("Thread started\n" + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime()))
    outputData = open("DatiUCI/conversionTable " + str(lb) + "-" + str(ub) + ".txt", "w")
    try:
        for i in range(lb, ub + 1):
            id = searchId(legend[i].split(" ")[2].strip('\n'))
            outputData.write(str(i + 1) + " " + str(id) + "\n")
    except Exception as err:
        print(err)
    outputData.close()
    print("From " + str(lb) + " to " + str(ub) + " done!\n" + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime()))
    
print("Creating conversion table...\n" + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime()))
inputData = open("DatiUCI/legendPermGenLevel0APIGenLevel1.txt", "r")
legend = []
while 1:
    line = inputData.readline()
    if len(line) == 0:
        break
    legend.append(line)
inputData.close()

# Launching threads
threads = []
for i in range(0, 100000, 1000):
    thread = threading.Thread(target = createConvTable, args = (i + 1, i + 1000))
    thread.start()
    threads.append(thread)

# Waiting threads to finish
for t in threads:
    t.join()

# Copying all parts of the conversion table into 1 file
outputData = open("DatiUCI/conversionTable.txt","w")
for i in range(0, 100000, 1000):
    inputData = open("DatiUCI/conversionTable " + str(i + 1) + "-" + str(i + 1000) + ".txt", "r")
    while 1:
        line = inputData.readline()
        if len(line) == 0:
            break
        outputData.write(line)
    inputData.close()
outputData.close()
print("Conversion table created!" + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime()))
