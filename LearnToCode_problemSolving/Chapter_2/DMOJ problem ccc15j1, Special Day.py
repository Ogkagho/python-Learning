#DMOJ problem ccc15j1, Special Day

month = int(input())
day = int(input())

if (month <= 2) and (day != 18):
    print('Before')
elif (month >=2 ) and (day != 18):
    print('After')
else:
    print('Special')

