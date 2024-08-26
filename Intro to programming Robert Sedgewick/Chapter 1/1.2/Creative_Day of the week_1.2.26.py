#Day of the week.

#1.2.26
import sys

m = int(sys.argv[1])
d = int(sys.argv[2])
y = int(sys.argv[3])

y_0 = y - (14 - m)/12
x = y_0 + y_0 - y_0/100 + y_0/400
m_0 = m + 12 *((14 - m)/12) - 2 
d_0 = (d + x + (31*m_0) /12) % 7

if d_0 == 1:
    print('Monday')
elif d_0 == 2:
    print('Tuesday')
elif d_0 == 3:
    print('Wednesday')
elif d_0 == 4:
    print('Thursday')
elif d_0 == 5:
    print('Friday')
elif d_0 == 6:
    print('Saturday')
elif d_0 == 0:
    print('Sunday')
