import numpy

# da matrice di numeri a matrice sparsa

def numbersToSparse(nameTxt, nameTxtToMatlab):
    # nameTxt = "data.txt"
    # nameTxtToMatlab = "dataToMatlab.txt"

    print("In " + nameTxt + " -> " + nameTxtToMatlab)

    dataTxt = open("../DatiUCI/anom/" + nameTxt, "r")
    dataToMatlab = open("..\\DatiUCI\\anom\\" + nameTxtToMatlab, "w")

    numFeature = 326110 + 1

    while True:
    # for i in range(1,5):
        line = dataTxt.readline()
        if len(line) == 0:
            break
        
        arrData = line.split()

        arrOut = numpy.zeros(numFeature, numpy.int8)  #riga di out

        arrOut[0] = int(arrData[0]) #Malware si/no

        # print(arrData)
        # print(".", flush=True, end=" ")

        for i in range(1, len(arrData)):
            index = int(arrData[i])
            arrOut[index] = 1

        dataToMatlab.write(" ".join(map(str, arrOut)) + "\n")

    dataTxt.close()
    dataToMatlab.close()

    print("End " + nameTxt + " -> " + nameTxtToMatlab)



arrStart = ['dataPermGenLevel0APIGenLevel1Reduced2000.txt', 
            'dataPermGenLevel0APIGenLevel2Reduced2000.txt',
            'dataPermGenLevel0APIGenLevel3Reduced2000.txt', 
            'dataPermGenLevel1APIGenLevel1Reduced2000.txt',
            'dataPermGenLevel1APIGenLevel2Reduced2000.txt', 
            'dataPermGenLevel1APIGenLevel3Reduced2000.txt',
            'dataPermGenLevel2APIGenLevel1Reduced2000.txt', 
            'dataPermGenLevel2APIGenLevel2Reduced2000.txt', 
            'dataPermGenLevel2APIGenLevel3Reduced2000.txt']

arrEnd = ['dataPermGenLevel0APIGenLevel1Reduced2000_sparse.txt', 
          'dataPermGenLevel0APIGenLevel2Reduced2000_sparse.txt',
          'dataPermGenLevel0APIGenLevel3Reduced2000_sparse.txt', 
          'dataPermGenLevel1APIGenLevel1Reduced2000_sparse.txt',
          'dataPermGenLevel1APIGenLevel2Reduced2000_sparse.txt', 
          'dataPermGenLevel1APIGenLevel3Reduced2000_sparse.txt',
          'dataPermGenLevel2APIGenLevel1Reduced2000_sparse.txt', 
          'dataPermGenLevel2APIGenLevel2Reduced2000_sparse.txt', 
          'dataPermGenLevel2APIGenLevel3Reduced2000_sparse.txt']


for i in range(0, len(arrStart)):
    numbersToSparse(arrStart[i], arrEnd[i])