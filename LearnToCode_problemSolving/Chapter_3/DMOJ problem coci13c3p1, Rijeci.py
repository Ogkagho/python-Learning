#DMOJ problem coci13c3p1, Rijeci
n = int(input())

word = 'A'
for i in range(n):
    newstr = ''
    for char in word:
        if char == 'A':
            newstr += 'B'
        else:
            newstr += 'BA'
    word = newstr
    
            
print(word.count('A'),word.count('B'))
