from multiprocessing import Process
import os
import time

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

# Function for searching id knowing name
def searchId(legend, name):
    for i in range(0, len(legend)):
        if legend[i].split(" ")[2].strip('\n') == name:
            return i + 1

# Process for creating part of the conversion table
def createConvTable(legend, lb, ub):
    info("Process started\n" + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime()))
    outputData = open("DatiUCI/conversionTable " + str(lb + 1) + "-" + str(ub + 1) + ".txt", "w")
    try:
        for i in range(lb, ub + 1):
            id = searchId(legend, legend[i].split(" ")[2].strip('\n'))
            outputData.write(str(i + 1) + " " + str(id) + "\n")
    except Exception as err:
        print(err)
        print(i)
    outputData.close()
    print("From " + str(lb + 1) + " to " + str(ub + 1) + " done!\n" + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime()))
    
if __name__ == '__main__':
    print("Creating conversion table...\n" + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime()))
    inputData = open("DatiUCI/legendPermGenLevel1APIGenLevel1.txt", "r")
    legend = []
    while 1:
        line = inputData.readline()
        if len(line) == 0:
            break
        legend.append(line)
    inputData.close()

    # Launching threads
    processes = []
    info('main line')
    for i in range(0, 326000, 2000):
        p = Process(target = createConvTable, args = (legend, i, i + 2000 - 1))
        p.start()
        processes.append(p)
    p = Process(target = createConvTable, args = (legend, 326000, 326109))
    p.start()
    processes.append(p)

    # Waiting processes to finish
    for p in processes:
        p.join()

    # Copying all parts of the conversion table into 1 file
    outputData = open("DatiUCI/conversionTable.txt","w")
    for i in range(0, 326000, 2000):
        inputData = open("DatiUCI/conversionTable " + str(i + 1) + "-" + str(i + 2000) + ".txt", "r")
        while 1:
            line = inputData.readline()
            if len(line) == 0:
                break
            outputData.write(line)
    inputData.close()
    inputData = open("DatiUCI/conversionTable 326001-326110.txt", "r")
    while 1:
        line = inputData.readline()
        if len(line) == 0:
            break
        outputData.write(line)
    inputData.close()
    outputData.close()
    print("Conversion table created!\n" + time.strftime("%d/%m/%Y %H:%M:%S", time.localtime()))
    input("Press Enter to continue...")
