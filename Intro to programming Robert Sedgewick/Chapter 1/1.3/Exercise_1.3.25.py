#Modify factors.py to write just one copy each of the prime divisors.

#1.3.25
import sys

n = int(sys.argv[1])

factor =  2
while factor**2 <= n:
    while (n % factor) == 0:
        
        n //= factor 
        if not (n % factor) == 0: 
            print(str(factor) + ' ')
    factor += 1
    
if n > 1:
    print(n)
print()
