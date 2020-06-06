listOfList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

AddRow1 = 0
AddRow2 = 0
AddRow3 = 0

for x in range(0,3):
    for y in range(0,3):
        #print( listOfList[x][y], end=' ')
        if   x == 0:
            AddRow1 = AddRow1 + listOfList[x][y]
        elif x == 1:
            AddRow2 = AddRow2 + listOfList[x][y]
        elif x == 2:
            print( listOfList[x][y], "  ")
            AddRow3 = AddRow3 +listOfList[x][y]

print("AddRow1: ", AddRow1) #11
print("AddRow2: ", AddRow2) #14
print("AddRow3: ", AddRow3) #17