#DMOJ problem ccc11s2, Multiple Choice

n = int(input())

count = 0
string =''
for i in range(2*n):
    string += input()

for i in range(n):
    if string[i] == string[-n+i]:
        count += 1
print(count)

