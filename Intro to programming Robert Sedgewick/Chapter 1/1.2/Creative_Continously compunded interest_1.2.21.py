#continuosly compounded interest
#Compose a program that calculates 
#and writes the amount of money you would have if you invested it at a given in
#terest rate compounded continuously, taking the number of years t, the principal 
#P, and the annual interest rate r as command-line arguments. The desired value is 
#given by the formula Pe^rt.

#1.2.21
import math

principal = float(input('Enter the pricipal amount: '))
rate = float(input('Enter the interest rate: '))
number_years = int(input('Enter the number of years: '))

amount = principal*math.e**(rate*number_years)

print("The amount after ", number_years, "is", amount)
