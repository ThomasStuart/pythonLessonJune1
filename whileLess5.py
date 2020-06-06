num = 0

# check 1:  0 <= 5  TRUE  , print( 0 )  , num -> 2
# check 2:  2 <= 5  TRUE  , print( 2 )  , num -> 4
# check 3:  4 <= 5  TRUE  , print( 4 )  , num -> 6
# check 4:  6 <= 5  FALSE ---- STOP
while (num <= 5):
    print(num)
    num += 2

