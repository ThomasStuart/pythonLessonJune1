def squareNum( num ):
    sqr = num * num
    return sqr

currNum = 2

# write a while loop that checks if the square of the
# current number is less than 100

print("Starting ...")

#     2  <  100  -> TRUE
#     4  <  100  -> TRUE
#     16 <  100  -> TRUE
#    256 <  100  -> FALSE

print(currNum)

while squareNum(currNum) < 100:
    currNum = squareNum(currNum)
    print(currNum)

print("...Ending")
# 2 -> 4 -> 16 -> 256
#2
#4
#16
#-----