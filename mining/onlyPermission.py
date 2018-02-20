dataPermission = open("DatiUCI/dataOnlyPermission.txt", "w")
dataReduced = open("DatiUCI/dataReduced500.txt", "r")


while True:
    resultString = ""
    line = dataReduced.readline()
    if len(line) == 0:
        break
    split = line.split(" ")

    for i in range (0, 114):
        resultString += split[i] + " "
    
    dataPermission.write(resultString + "\n")
 
dataReduced.close()
dataPermission.close()