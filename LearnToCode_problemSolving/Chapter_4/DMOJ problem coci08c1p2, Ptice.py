#DMOJ problem coci08c1p2, Ptice
n = int(input())
string = input()

adrian = 'ABC'
bruno = 'BABC'
goran = 'CCAABB'

countA = countB = countG = 0

for i in range(n):
    if string[i] == adrian[i % len(adrian)]:
        countA += 1
    if string[i] == bruno[i % len(bruno)]:
        countB += 1
    if string[i] == goran[i % len(goran)]:
        countG += 1

M = max(countA, countB, countG)
print(M)

if M == countA:
    print('Adrian')
if M == countB:
    print('Bruno')
if M == countG:
    print('Goran')
