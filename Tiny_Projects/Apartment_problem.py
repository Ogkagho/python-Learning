

 def maximizeProfit():
     """
     Function to calculate the number of units to be rented 
     to maximize profits.
     Assumes initial number of units is 50.
     prarameters: The rent to occupy all the units.
                  The increase in rent that results in a vacant unit.
                  Amount to maintain a rented unit.
     return a tuple, of the maximum profit and the number of units 
     """
     rentOccupy = float(input('Enter the amount of rent to occupy all the units: '))
     increaseRent = float(input('Enter the increase in rent that results in a vacant unit: '))
     maintain = float(input('Enter the amount to maintain a rented unit: '))
     maxProfit = 0
     optimalUnits = 0
         
     for i in range(50):
         n = (50 - i)
         profit = n*(rentOccupy - maintain)
         if profit > maxProfit:
             maxProfit = profit
             optimalUnits = n
         rentOccupy += increaseRent
         
     print(f'The number of units to be rented to maximize profit is {optimalUnits} units.')
 

    

 


