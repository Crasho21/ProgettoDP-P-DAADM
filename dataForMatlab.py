import numpy

dataTxt = open("DatiUCI/data.txt", "r")
dataToMatlab = open("DatiUCI/dataToMatlab.txt", "w")

numFeature = 326110 + 1

while True:
# for i in range(1,5):
    line = dataTxt.readline()
    if len(line) == 0:
        break
    
    arrData = line.split(" ")

    arrOut = numpy.zeros(numFeature, numpy.int8)  #riga di out

    arrOut[0] = int(arrData[0]) #Malware si/no

    # print(arrData)
    # print(".", flush=True, end=" ")

    for i in range(1, len(arrData)-1):
        index = int(arrData[i])
        arrOut[index] = 1

    dataToMatlab.write(" ".join(map(str, arrOut)) + "\n")

    
dataTxt.close()
dataToMatlab.close()


