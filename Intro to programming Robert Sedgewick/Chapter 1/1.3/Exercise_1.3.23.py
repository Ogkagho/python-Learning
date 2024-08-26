#Modify gambler.py to take an extra command-line argument that specifies
#the (fixed) probability that the gambler wins each bet. Use your program to 
#try to learn how this probability affects the chance of winning and the expected 
#number of bets. Try a value of p close to 0.5 (say, 0.48)

#1.3.23
import random
import sys

stake = int(sys.argv[1])
goal = int(sys.argv[2])
trials = int(sys.argv[3])
fixed_prob = float(sys.argv[4])

wins = 0
total_cash = 0
total_bets = 0

for t in range(trials):
    cash = stake
    bets = 0
    while (cash > 0) and (cash < goal):
        bets += 1
        if random.random() < fixed_prob:  #Uses random.random() for probability check
            cash += 1
        else:
            cash -= 1
    if cash == goal:
        wins += 1
    total_cash += cash
    total_bets += bets  # Accumulate total bets correctly

print(f"{100 * wins // trials}% wins")
print(f"Avg # bets: {total_bets // trials}")

