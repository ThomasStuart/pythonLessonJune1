

words    = [  'i' , 'am' ,   'not' , 'the' ,   'EXIT' , 'but' , 'it' , 'is' , 'in' , 'EXIT']
budget  = [    80 ,    20,    600,       3,      800,    70,    44,    12 ]
#                                                 ^

# END the while loop when you encounter a pair where the number is greater than 500 and the word is  exit
i = 0


while (i < len(words)  ) and (i < len( budget)) :
    if budget[i] > 500  and  words[i] == 'EXIT' :
        break

    print( budget[i] , words[i])
    i = i + 1