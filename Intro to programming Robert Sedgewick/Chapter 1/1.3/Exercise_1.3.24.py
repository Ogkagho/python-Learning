#Modify gambler.py to take an extra command-line argument that specifies
#the number of bets the gambler is willing to make, so that there are three possible 
#ways for the game to end: the gambler wins, loses, or runs out of time. Add to 
#the output to give the expected amount of money the gambler will have when the 
#game ends. Extra credit : Use your program to plan your next trip to Monte Carlo.

#1.3.24
import random

stake = int(input('Enter your stake: '))
goal = int(input('Enter your goal: '))
trials = int(input('Enter the number of trials you want to perform: '))
upperlimit = int(input('Enter the nnumber of bets you are willing to make: '))

total_bets = 0
wins = 0
total_cash = 0

for t in range(trials):
    cash = stake
    bets = 0
    while (cash > 0) and (cash < goal) and (bets < upperlimit):
        bets += 1
        if random.randrange(0, 2) == 0:
            cash += 1
        else:
            cash -= 1
    if cash == goal:
        wins += 1
    total_cash += cash
    total_bets += bets

print(str(100 * wins / trials) + '% wins')
print('Avg # bets: ' + str(total_bets//trials))
print('How much money gambler takes home,', total_cash/trials)
