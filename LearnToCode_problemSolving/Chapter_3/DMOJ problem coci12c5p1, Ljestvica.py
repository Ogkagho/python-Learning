#DMOJ problem coci13c3p1, Rijeci

string = input()

countC = 0
countA = 0
for i in range(len(string),3):
    if string[i] == 'A' or string[i] == 'D' or string[i] == 'E':
        countC += 1
    elif string[i] == 'C' or string[i] == 'F' or string[i] == 'G':
        countA += 1

if countC > countA:
    print('C-dur')
elif countC < countA:
    print('A-mol')
else:
    if string[-1] == 'A':
        print('A-mol')
    elif string[-1] == 'C':
        print('C-dur')

