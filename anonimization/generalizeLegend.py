import pymongo
from pymongo import MongoClient
from pprint import pprint
import threading
import time

def search(name):
    for i in range(0, len(permLevels)):
##        print(permLevels[i].split(" ")[0] + " == " + name)
        if permLevels[i].split(" ")[0] == name:
            return permLevels[i].split(" ")[1]

# Permission and API generalization levels
permGenLevel = 2
apiGenLevel = 3

print("Generalizing legend...\n" + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime()) + "\n")
inputData = open("DatiUCI/legend.txt", "r")
legend = []
while 1:
    line = inputData.readline()
    if len(line) == 0:
        break
    legend.append(line)
inputData.close()

inputData = open("DatiUCI/legendPermissionsGeneralizationLevel1.txt", "r")
permLevels = []
while 1:
    line = inputData.readline()
    if len(line) == 0:
        break 
    permLevels.append(line)

for i in range(0, 114):
    if permGenLevel == 1:
        temp = search(legend[i].split(" ")[2].strip('\n'))
        legend[i] = legend[i].split(" ")[0] + " " + legend[i].split(" ")[1] + " " + temp.strip('\n')
##        print(legend[i].strip('\n') + " -> " + legend[i].split(" ")[0] + " " + legend[i].split(" ")[1] + " " + temp.strip('\n'))
    elif permGenLevel == 2:
        legend[i] = legend[i].split(" ")[0] + " " + legend[i].split(" ")[1] + " permission"

for i in range(114, len(legend)):
    if apiGenLevel == 3:
        legend[i] = legend[i].split(" ")[0] + " " + legend[i].split(" ")[1] + " api"
    else:
##        print(legend[i].strip('\n'), end = ' -> ')
        temp = legend[i]
        if apiGenLevel > 0:
            temp = legend[i].split("->")[0]
        temp = temp.split(".")
        temp2 = ""
        level = apiGenLevel - 1
        if level < 0:
            level = 0
        for j in range(0, len(temp) - level):
            temp2 += temp[j] + "."
        temp2 = temp2.strip('\n')
        legend[i] = temp2[0 : -1]
##        print(temp2[0 : -1])
##        print(legend[i])

outputData = open("DatiUCI/legendPermGenLevel" + str(permGenLevel) + "APIGenLevel" + str(apiGenLevel) + ".txt", "w")
try:
    for i in range(0, len(legend)):
        outputData.write(legend[i].strip('\n') + "\n")
except Exception as err:
    print(err)
outputData.close()

print("Legend generalized! Permission generalization level " + str(permGenLevel) + " API generalization level " + str(apiGenLevel) + "\n" + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime()) + "\n")
