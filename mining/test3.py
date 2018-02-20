# dataAPI = open("DatiUCI/dataOnlyAPI.txt", "w")
dataReduced = open("DatiUCI/dataTest5000.txt", "w")

resultString = ""

i=0
temp=""
for j in range (1, 5000):
    temp += " " + str(1)

for i in range (1, 5000):
    dataReduced.write(temp + "\n")

dataReduced.close()
# dataAPI.close()