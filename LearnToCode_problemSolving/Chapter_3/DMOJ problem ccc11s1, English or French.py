#DMOJ problem ccc11s1, English or French
n = int(input())
countT = 0
countS = 0
for i in range(n):
    string = input()
    for i in string:
        if i == 'T' or i == 't':
            countT += 1
        elif i == 'S'  or i == 's':
            countS += 1

if countT > countS:
    print('English')
elif countT < countS:
    print('French')
else:
    print('French')
