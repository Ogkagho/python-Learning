#Expand your solution to the “Continuously compounded interest” exercise 
#from section 1.2 (exercise 1.2.21) to write a table giving the total amount paid and 
#the remaining principal after each monthly payment

#1.3.14

principal = float(input('Enter the pricipal amount: '))
rate = float(input('Enter the interest rate: '))
number_years = int(input('Enter the number of years: '))

monthly_rate = rate/12
number_months = number_years * 12

for i in range(1, number_months+1):
    amount = principal*math.e**(i*monthly_rate)
    principal -= amount 
    print(f"{i:<10}{amount:<20.2f}{principal:<20.2f}")
