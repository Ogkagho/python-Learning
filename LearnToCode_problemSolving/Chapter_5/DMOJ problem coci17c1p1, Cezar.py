#DMOJ problem coci17c1p1, Cezar

cards_drawn = int(input())

card = [0, 0]
card += [4]*10
sum1 = 0

for i in range(cards_drawn):
    drawn = int(input())
    card[drawn] -= 1 
    sum1 += drawn

X = 21 - sum1
sum2 = 0
for i in range(X+1, len(card)):
    sum2 += card[i]

sum3 = 0
for i  in range(2, X):
    sum3 += card[i]

if sum2 >= sum3:
    print('DOSTA')
else:
    print('VUCI')
