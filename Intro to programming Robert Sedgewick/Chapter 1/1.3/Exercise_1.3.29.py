#Compose a program relativelyprime.py that takes one command-line 
#argument n and writes an n-by-n table such that there is an * in row i and column 
#j if the gcd of i and j is 1 (i and j are relatively prime), and a space in that position 
#otherwise.


#1.3.29

for x in range(1, 4):  # set values for rows
    for y in range(1, 4): #set values for columns 
        i = x   #variables to check for gcd
        j = y   
        while j != 0:   #gcd starts checking 
            if i > j == 0:
                if i % j == 0 and j == 1:
                    print('* ', end ='')
                    break
                elif i % j == 0:
                    print('  ', end = '')
                else:
                    i, j = j, i % j 
            else:
                i, j = j, i % j 
        if j == 0 and i == 1:
            print('* ', end ='')
        elif j == 0:
            print('  ', end = '')
    print()

#I know i know, i could have ued a function to check the gcd to make the
#program simpler, but functions haven't been introduced, so deal with it :)
