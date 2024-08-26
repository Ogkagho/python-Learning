#DMOJ problem ccc19j3, Cold Compress
n = int(input())

for i in range(n):
    string = input()
    char = string[0]
    count = 1
    i = 1
    while i < len(string):
        if string[i] == char:
            count += 1
        else:
            print(count, char, end=' ')
            char = string[i]
            count = 1
        if i == len(string) - 1:
            print(count, char)
        i += 1
