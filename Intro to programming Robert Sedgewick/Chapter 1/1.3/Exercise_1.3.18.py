#Using Newton’s method, develop a program that takes integers n and k as 
#command-line arguments and writes the kth root of n
#If you know calculus, newtons method, you know how i got this ;)

#1.3.18
#k-th root using newtons method
c = int(sys.argv[1])
k = int(sys.argv[2])
EPSILON = 1e-10
t = c
r = k - 1

while abs((t**k) - c) > (EPSILON):
    t = 1/k * (r*t + c/(t**r))
    
print('The ' + str(k) + ' root of ' + str(c) + ' is '
            + str(t))
