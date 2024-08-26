#DMOJ problem ccc15j2, Happy or Sad

line = input()

sadCount = line.count(':-(')
happyCount = line.count(':-)')

if sadCount > happyCount:
    print('sad')
elif sadCount < happyCount:
    print('Happy')
elif sadCount == 0 and happyCount == 0:
    print('none')
else:
    print('Unsure')

