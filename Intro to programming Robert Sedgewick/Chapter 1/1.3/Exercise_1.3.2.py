#Compose a more general and more robust version of quadratic.py 
#(program 1.2.4) that writes the roots of the polynomial ax2 + bx + c, writes an ap
#propriate message if the discriminant is negative, and behaves appropriately (avoid
#ing division by zero) if a is zero

#1.3.2
#Quadratic
import sys
a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

if a == 0:
    print('This is not a quadratic equation.')
else:
    d = b*b - 4*a*c
    if d < 0:
        print('The equation has no real roots')
    elif d == 0:
        print('The equation has a repeated root')
        print(str((-b+d)/2.0))
    else:
        print('The equation has two distinct roots')
        print(str((-b+d)/2.0) + ' and ' + str((-b-d)/2.0))


