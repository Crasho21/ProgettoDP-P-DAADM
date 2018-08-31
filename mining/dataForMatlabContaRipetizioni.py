import numpy
# numpy.set_printoptions(threshold=numpy.nan) #stampa array numpy senza abbreviazioni 

def numbersToSparse(nameTxt, nameTxtToMatlab):
    print("In " + nameTxt + " -> " + nameTxtToMatlab)

    dataTxt = open("../DatiUCI/anom/" + nameTxt, "r")
    dataToMatlab = open("..\\DatiUCI\\anom\\counttest\\" + nameTxtToMatlab, "w")

    numFeature = 326110 + 1

    while True:
    # for i in range(1,5):
        line = dataTxt.readline()
        if len(line) == 0:
            break
        
        arrData = line.split()

        # print(arrData)

        arrOut = numpy.zeros(numFeature, numpy.int16)  #riga di out

        arrOut[0] = int(arrData[0]) #Malware si/no

        # print(arrData)
        # print(".", flush=True, end=" ")

        for i in range(1, len(arrData)):
            index = int(arrData[i])
            arrOut[index] = arrOut[index]+1
            if(arrOut[index]<0): print("alarm!")

            # print("+1")
            # for i in range(0, 1000):
            #     if(arrOut[i] != 0): print(arrOut[i], end=' ')

        # print("line")
        # for i in range(0, len(arrOut)):
        #     if(arrOut[i] != 0): print(arrOut[i], end=' ')

        # print()

        dataToMatlab.write(" ".join(map(str, arrOut)) + "\n")

    print("End " + nameTxt + " -> " + nameTxtToMatlab)
        
    dataTxt.close()
    dataToMatlab.close()



arrStart = ['dataPermGenLevel0APIGenLevel2Reduced2000.txt',
            'dataPermGenLevel0APIGenLevel1Reduced2000.txt', 
            
            'dataPermGenLevel0APIGenLevel3Reduced2000.txt', 
            'dataPermGenLevel1APIGenLevel1Reduced2000.txt',
            'dataPermGenLevel1APIGenLevel2Reduced2000.txt', 
            'dataPermGenLevel1APIGenLevel3Reduced2000.txt',
            'dataPermGenLevel2APIGenLevel1Reduced2000.txt', 
            'dataPermGenLevel2APIGenLevel2Reduced2000.txt', 
            'dataPermGenLevel2APIGenLevel3Reduced2000.txt']

arrEnd = [
          'dataPermGenLevel0APIGenLevel2Reduced2000_sparse_count.txt',
          'dataPermGenLevel0APIGenLevel1Reduced2000_sparse_count.txt', 
          'dataPermGenLevel0APIGenLevel3Reduced2000_sparse_count.txt', 
          'dataPermGenLevel1APIGenLevel1Reduced2000_sparse_count.txt',
          'dataPermGenLevel1APIGenLevel2Reduced2000_sparse_count.txt', 
          'dataPermGenLevel1APIGenLevel3Reduced2000_sparse_count.txt',
          'dataPermGenLevel2APIGenLevel1Reduced2000_sparse_count.txt', 
          'dataPermGenLevel2APIGenLevel2Reduced2000_sparse_count.txt', 
          'dataPermGenLevel2APIGenLevel3Reduced2000_sparse_count.txt']

for i in range(0, len(arrStart)):
    numbersToSparse(arrStart[i], arrEnd[i])