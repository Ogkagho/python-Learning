#divisor pattern

#1.3.15 

n = int(sys.argv[1])

i = 1
while i <= n:
    j = 1
    while j <= n:
        if (i %  j == 0) or (j % i == 0):
            stdio.write('* ')
        else:
            stdio.write('  ')
        j += 1
    stdio.writeln(i)
    i += 1
