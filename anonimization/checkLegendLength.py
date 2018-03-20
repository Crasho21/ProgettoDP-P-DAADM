inputData = open("DatiUCI/legendPermGenLevel0APIGenLevel3.txt", "r")
legend = []
while 1:
    line = inputData.readline()
    if len(line) == 0:
        break
    legend.append(line)
inputData.close()
print(len(legend))
