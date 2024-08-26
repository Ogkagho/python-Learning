#DMOJ problem coci18c4p1, Elder
obeyWand = input()
n = int(input())
dueled =''
for i in range(n):
    duelWand = input()
    if obeyWand in duelWand:
        obeyWand = duelWand[0]
        if obeyWand not in dueled:
            dueled += duelWand[0]
print(obeyWand)
print(len(dueled))

