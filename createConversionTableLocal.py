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

print("Creating conversion table...\n" + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime()))
inputData = open("DatiUCI/legend.txt", "r")
legend = []
while 1:
    line = inputData.readline()
    if len(line) == 0:
        break
    legend.append(line)
inputData.close()

outputData = open("DatiUCI/conversionTable.txt", "w")
try:
    for i in range(0, len(legend)):
        id = searchId(legend[i].split(" ")[2].strip('\n'))
        outputData.write(str(i + 1) + " " + str(id) + "\n")
except Exception as err:
    print(err)
outputData.close()

print("Conversion table created!" + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime()))
