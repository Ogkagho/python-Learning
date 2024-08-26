#DMOJ problem wc17c3j3, Uncrackable
string = input()

assert len(string) < 8 or len(string) > 12, 'Invalid'

countUpper = 0
countLower = 0
countDigit = 0

for char in string:
    if char.isupper():
        countUpper += 1
    elif char.islower():
        countLower += 1
    else:
        countDigit += 1 
if countLower >= 3 and countUpper >= 2 and countDigit >= 1:
    print('Valid')
else:
    print('Invalid')

