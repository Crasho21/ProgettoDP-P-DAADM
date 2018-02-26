import sys

# Read permissions in legend
print("Reading legend...", end = ' ')
inputLegend = open("legendPermissions.txt","r")
legend = []
while 1:
    line = inputLegend.readline()
    if len(line) == 0:
        break
    temp = line.split(" ")
    legend.append(temp[2].strip('\n'))
inputLegend.close()
print("Complete!")
print(len(legend))

# Read permissions in categories
print("Reading categories...", end = ' ')
inputCategoriess = open("protection_level_to_permission_mapping.txt","r")
categories = []
while 1:
    line = inputCategoriess.readline()
    if len(line) == 0:
        break
    categories.append(line.strip('\n'))
inputCategoriess.close()
print("Complete!")
print(len(categories))

# Checking if legend is completely included in categories
missingPermissions = []
for i in range (0, len(legend)):
    missing = True
    for j in range (0, len(categories)):
        if(legend[i] == categories[j]):
            missing = False
            break
    if(missing):
##        print(legend[i] + " (permission " + str(i) + ") is missing from categories...")
##        sys.exit()
        missingPermissions.append(legend[i] + " (permission " + str(i) + ")")

# Print result
if len(missingPermissions) == 0:
    print("Every permission is in categories")
else:
    for i in range (0, len(missingPermissions)):
        print(missingPermissions[i])
