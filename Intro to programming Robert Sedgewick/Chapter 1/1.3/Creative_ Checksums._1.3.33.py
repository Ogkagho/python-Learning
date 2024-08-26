#Checksums

#1.3.33

n = input()

sum1 = 0
for i in range(len(n)):
    sum1 += (10 - i)*int(n[i])
for i in range(0, 10):
    sum1 += i
    if sum1 % 11 == 0:
        checksum = i
        break
    else:
        sum1 -= i
print(n + str(i))
