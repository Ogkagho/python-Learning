#DMOJ problem ccc07j3, Deal or No Deal Calculator

cases_opened = int(input())

dollar_amounts = [0, 100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]

count1 = 1
for i in range(cases_opened):
    n = int(input())
    dollar_amounts[n] = 0
    count1 += 1

bankersOffer = int(input())

average = sum(dollar_amounts) / (len(dollar_amounts) - count1)

if average > bankersOffer:
    print('no deal')
else:
    print('deal')
