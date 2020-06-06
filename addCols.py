listOfList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

AddCol1 = 0
AddCol2 = 0
AddCol3 = 0

for x in range(0,3):
    for y in range(0,3):
        if y == 0:
            AddCol1 = AddCol1 + listOfList[x][y]
        elif y == 1:
            AddCol2 = AddCol2 + listOfList[x][y]
        elif y == 2:
            AddCol3 = AddCol3 + listOfList[x][y]


print("AddCol1: ", AddCol1)  #12
print("AddCol2: ", AddCol2 ) #15
print("AddCol3: ", AddCol3 ) #18