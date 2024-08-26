#DMOJ problem coci18c3p1, Magnus
string = input()

count = 0
word = 'HONI'
step = 0
body = 0
for i in string:
    if i  == word[step]:
        step += 1
    if step == 4:
        count += 1
        step = 0
print(count)

