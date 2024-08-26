#Trigonometric functions
#Compose programs sine.py and cosine.py 
#that compute the sine and cosine functions using their Taylor series expansions  
#sin x = x - x^3/3! + x^5/5! - … and cos x = 1 - x^2/2! +  x^4/4! - . . .


#1.3.38
#sine function

x = float(input('Enter to compute sin(x): '))
sin = x
fact = 1
count = 1

for i in range(3,50,2):
    fact *= i * (i - 1) 
    sin += (-1)**count *(x**i / fact)
    count += 1

print(sin)


#cosine function
x = float(input('Enter To compute cos(x): '))
cos = 1
fact = 1
count = 1

for i in range(2, 50, 2):
    fact *= i * (i - 1)
    cos += (-1)**count*(x**i / fact)
    count += 1

print(cos)
