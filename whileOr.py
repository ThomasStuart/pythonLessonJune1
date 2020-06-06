

words   = ['i' , 'am' , 'not' , 'the' , 'EXIT' , 'but' , 'it' , 'is' , 'in' , 'list']
budget  = [80 ,     20,    77,     3,    30 ,     50  ,  100  ]

# while the clause to the traverse the while loop and print the
# words until the word 'end' is visited OR the a number in budget is less than 100

i = 0


while (i < len(words)  ) and (i < len( budget)) :
    if budget[i] > 100  or  words[i] == 'EXIT' :
        break
    print( budget[i] , words[i])
    i = i + 1

# AND
# TRUE FALSE  -> FALSE
# FALSE TRUE  -> FALSE
# FALSE FALSE -> FALSE
# TRUE  TRUE  -> TRUE

# TRUE FALSE  FALSE -> FALSE
# FALSE TRUE  TRUE ->  FALSE
# FALSE FALSE FALSE->  FALSE
# TRUE  TRUE  TRUE ->  TRUE

# OR
# TRUE FALSE  -> TRUE
# FALSE TRUE  -> TRUE
# FALSE FALSE -> FALSE
# TRUE  TRUE  -> TRUE

