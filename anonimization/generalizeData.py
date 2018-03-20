import time

print("Generalizing data...\n" + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime()) + "\n")
inputData = open("DatiUCI/data.txt", "r")
data = []
i = 0
while 1:
    line = inputData.readline()
    if len(line) == 0:
        break
    data.append(line)
    i += 1
inputData.close()

inputData = open("DatiUCI/conversionTablePermGenLevel2APIGenLevel3.txt", "r")
conversionTable = []
while 1:
    line = inputData.readline()
    if len(line) == 0:
        break 
    conversionTable.append(line.split(" ")[1])
inputData.close()

for i in range(0, len(data)):
    temp = data[i][2 : -2].split(" ")
    temp2 = data[i][0]
    for t in temp:
        t = conversionTable[int(t) - 1].strip('\n')
        temp2 += " " + t
##    print(data[i])
##    print(temp2)
    data[i] = temp2

outputData = open("DatiUCI/generalizedData.txt", "w")
try:
    for i in range(0, len(data)):
        outputData.write(data[i] + "\n")
except Exception as err:
    print(err)
outputData.close()

print("Data generalized!\n" + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime()) + "\n")
