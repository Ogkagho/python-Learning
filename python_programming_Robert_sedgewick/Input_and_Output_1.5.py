# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 16:46:24 2024

@author: Lenovo
"""

import sys
sys.path.append('C:\\Users\\Lenovo\\Downloads\\introcs-1.0')

import stdio
import random
import math
import stddraw 
import stdarray

# =============================================================================
# RANGE = 1000000
# 
# secret = random.randrange(1, RANGE+1)
# stdio.write('I am thinking of a secret number between 1 and ')
# stdio.writeln(RANGE)
# 
# guess = 0
# while guess != secret:
#     stdio.write('What is your guess? ')
#     guess = stdio.readInt()
#     
#     if (guess < secret): stdio.writeln('Too low')
#     elif (guess > secret): stdio.writeln('Too high')
#     else:stdio.writeln('You win!')
# =============================================================================
    
# =============================================================================
# #Draws a triangle whith a point at the center  
# t = math.sqrt(3.0) / 2
# stddraw.line(0.0, 0.0, 1.0, 0.0)
# stddraw.line(1.0, 0.0, 0.5, t)
# stddraw.line(0.5, t, 0.0, 0.0)
# stddraw.point(0.5, t/3.0)
# stddraw.show()
# =============================================================================

# =============================================================================
# #plotfilter
# x0 = stdio.readFloat()
# y0 = stdio.readFloat()
# x1 = stdio.readFloat()
# y1 = stdio.readFloat()
# stddraw.setXscale(x0, x1)
# stddraw.setYscale(y0, y1)
# 
# stddraw.setPenRadius(0.0)
# while not stdio.isEmpty():
#     x = stdio.readFloat()
#     y = stdio.readFloat()
#     stddraw.point(x, y)
# 
# stddraw.show()
# =============================================================================


#Function graph
n = int(sys.argv[1])

x = stdarray.create1D(n+1, 0.0)
y = stdarray.create1D(n+1, 0.0)

for i in range(n+1):
    x[i] = math.pi * i /n
    y[i] = math.sin(4.0*x[i]) + math.sin(20.0*x[i]) 
stddraw.setXscale(0, math.pi)
stddraw.setYscale(-2.0, 2.0)
for i in range(n):
    stddraw.line(x[i], y[i], x[i+1], y[i+1])
stddraw.show()
    
    
