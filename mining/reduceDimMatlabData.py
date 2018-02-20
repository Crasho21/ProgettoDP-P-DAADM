dataToMatlab = open("../DatiUCI/data.txt", "r")
dataReduced = open("../DatiUCI/data5000.txt", "w")

n = 2500

# for i in range(1,5):
for i in range(0,n):
    line = dataToMatlab.readline()
    dataReduced.write(line)

while True:
    line = dataToMatlab.readline()
    if(int(line[0]) == 0): break

for i in range(0,n):
    line = dataToMatlab.readline()
    dataReduced.write(line)

dataReduced.close()
dataToMatlab.close()