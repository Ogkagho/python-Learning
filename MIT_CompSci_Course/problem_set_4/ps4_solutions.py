# Problem Set 4
# Name: 
# Collaborators: 
# Time: 

#
# Problem 1
#

def nestEggFixed(salary, save, growthRate, years):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: the annual percent increase in your investment account (an
      integer between 0 and 100).
    - years: the number of years to work.
    - return: a list whose values are the size of your retirement account at
      the end of each year.
    """
    retireFund = [0.0]*(years)
    mult = salary*save*0.01
    retireFund[0] = mult
    mult1 = (1+ 0.01*growthRate)
    for i in range(1,years):
        retireFund[i] = retireFund[i-1] * mult1 + mult
    
    return retireFund

def testNestEggFixed():
    salary     = 10000
    save       = 10
    growthRate = 15
    years      = 5
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print(savingsRecord)
    # Output should have values close to:
    # [1000.0, 2150.0, 3472.5, 4993.375, 6742.3812499999995]

    # TODO: Add more test cases here.

#
# Problem 2
#

def nestEggVariable(salary, save, growthRates):
    # TODO: Your code here.
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: a list of the annual percent increases in your investment
      account (integers between 0 and 100).
    - return: a list of your retirement account value at the end of each year.
    """
    
    retireFund = [0.0]*(len(growthRates))
    mult = salary*save*0.01
    retireFund[0] = mult
    
    for i in range(1, len(growthRates)):
        retireFund[i] = retireFund[i-1] * (1+ 0.01*growthRates[i]) + mult
    
    return retireFund
    

def testNestEggVariable():
    salary      = 10000
    save        = 10
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print(savingsRecord)
    # Output should have values close to:
    # [1000.0, 2040.0, 3142.0, 4142.0, 5266.2600000000002]

    # TODO: Add more test cases here.

#
# Problem 3
#

def postRetirement(savings, growthRates, expenses):
    """
    - savings: the initial amount of money in your savings account.
    - growthRate: a list of the annual percent increases in your investment
      account (an integer between 0 and 100).
    - expenses: the amount of money you plan to spend each year during
      retirement.
    - return: a list of your retirement account value at the end of each year.
    """
    # TODO: Your code here.
    
    retireFund = [0.0]*(len(growthRates))
    retireFund[0] = savings*(1 + 0.01 *growthRates[0]) - expenses
    
    for i in range(1, len(growthRates)):
        retireFund[i] = retireFund[i-1] *(1 + 0.01 *growthRates[i]) - expenses
    
    return retireFund

def testPostRetirement():
    savings     = 100000
    growthRates = [10, 5, 0, 5, 1]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print(savingsRecord)
    # Output should have values close to:
    # [80000.000000000015, 54000.000000000015, 24000.000000000015,
    # -4799.9999999999854, -34847.999999999985]

    # TODO: Add more test cases here.

#
# Problem 4
#

def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates,
                    epsilon):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - preRetireGrowthRates: a list of annual growth percentages on investments
      while you are still working.
    - postRetireGrowthRates: a list of annual growth percentages on investments
      while you are retired.
    - epsilon: an upper bound on the absolute value of the amount remaining in
      the investment fund at the end of retirement.
    """
    # TODO: Your code here.
    
    ls = nestEggVariable(salary, save, preRetireGrowthRates)  #retunns list of preretirement funds
    endOfPre = ls[-1]    #assigns last years retirement fund amount 
    upperBound = ls[-1]  #becomes upperbound as savings for post retirement 
    lowerBound = 0
    expenses = (lowerBound + upperBound) / 2.0   #gets expense by averaging
    ls2 = postRetirement(endOfPre, postRetireGrowthRates, expenses) #tests expense
    
    while lowerBound < upperBound: #loop condition, assures loop ends
        print(ls2[-1], expenses)
        if ls2[-1] > epsilon:  
            lowerBound = expenses + 0.45
        else:
            upperBound = expenses - 0.45
        expenses = (lowerBound + upperBound) / 2.0
        ls2 = postRetirement(endOfPre, postRetireGrowthRates, expenses)
    
    return expenses
    

def testFindMaxExpenses():
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print(expenses)
    # Output should have a value close to:
    # 1229.95548986

    # TODO: Add more test cases here.
