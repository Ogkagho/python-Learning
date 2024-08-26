#Compose a program gamblerplot.py that traces a gambler’s ruin simula
#tion by writing a line after each bet in which one asterisk corresponds to each dollar 
#held by the gambler

#1.3.22
#gamblers ruin

import random
import sys

stake = int(sys.argv[1])
goal = int(sys.argv[2])
trials = int(sys.argv[3])

total_bets = 0
wins = 0
for t in range(trials):
    cash = stake
    bets = 0
    while (cash > 0) and (cash < goal):
        bets += 1
        if random.randrange(0,2) == 0:
            cash += 1
        else:
            cash -= 1
        print('*'*cash)
    print()
        
    if cash == goal:
        wins += 1
    total_bets += bets

stdio.writeln(str(100 * wins //trials) + '% wins')
stdio.writeln('Avg # bets: ' + str(total_bets // trials))

