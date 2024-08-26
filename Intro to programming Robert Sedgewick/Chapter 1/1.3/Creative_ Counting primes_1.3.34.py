#Counting Primes

#1.3.34
#Naive implementation
#sieve is more efficient

n = int(input('Enter:'))

countPrime = 0
if n > 2:
    countPrime = 1  # Counting 2 as a prime number

for i in range(3, n, 2):
    isPrime = True
    for j in range(3, int(math.sqrt(i)) + 1, 2):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        countPrime += 1

print(countPrime)

#also a function fto check primality
def isPrime(n):
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
    if n > 1:
        return True 
