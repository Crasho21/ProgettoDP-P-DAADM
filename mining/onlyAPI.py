dataAPI = open("DatiUCI/dataOnlyAPI.txt", "w")
dataReduced = open("DatiUCI/dataReduced500.txt", "r")

resultString = ""

while True:
    line = dataReduced.readline()
    if len(line) == 0:
        break
    split = line.split(" ")
    
    for i in range (1, 114):
        split[i] = "0"
    
    dataAPI.write(" ".join(split))
 
dataReduced.close()
dataAPI.close()