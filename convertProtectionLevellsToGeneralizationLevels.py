import pymongo
from pymongo import MongoClient
from pprint import pprint
import threading
import time

# Permission and API generalization levels
permGenLevel = 0
apiGenLevel = 0

print("Converting protection levels...\n" + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime()) + "\n")
inputData = open("DatiUCI/protection_level_to_permission_mapping.txt", "r")
outputData = open("DatiUCI/legendPermissionsGeneralizationLevel1.txt", "w")
while 1:
    line = inputData.readline()
    if len(line) == 0:
        break
    category = line[0 : -2]
    line = inputData.readline()
    rows = int(line.split(" ")[0])
    for i in range(0, rows):
        line = inputData.readline()
        outputData.write(line.strip('\n') + " " + category + "\n")
##        print(line.strip('\n') + " " + category)
outputData.close()
inputData.close()

print("Permissions generalization levels created!\n" + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime()) + "\n")
