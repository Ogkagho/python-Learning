
#1.3.41
#Game simulation mantyhall

#Game simulation. In the 1970s game show Let’s Make a Deal, a contestant 
#is presented with three doors. Behind one of them is a valuable prize. After the con
#testant chooses a door, the host opens one of the other two doors (never revealing 
#the prize, of course). The contestant is then given the opportunity to switch to the 
#other unopened door. Should the contestant do so? Intuitively, it might seem that 
#the contestant’s initial choice door and the other unopened door are equally likely 
#to contain the prize, so there would be no incentive to switch. Compose a program 
#montehall.py to test this intuition by simulation. Your program should take a 
#command-line argument n, play the game n times using each of the two strategies 
#(switch or do not switch), and write the chance of success for each of the two strategies


import random

n = int(input('Enter: '))
win = 0
#Simulates a game where the constestant doesn't switch
#1-3 is used to represent the choices behind the door
for i in range(n+1):
    prize = random.randrange(1,4)
    choice = random.randrange(1,4)     #Contestant choice 
    if choice == prize:
        win += 1
print(str(100*(win/n)) + ' % wins if no switch')
 
win = 0
for i in range(n+1): 
    prize = random.randrange(1,4)
    choice = random.randrange(1,4)
    presenterOpen = random.randrange(1,4)
    #Ensure the host does not open the door with the prize or the contestant's initial choice
    while presenterOpen == choice or presenterOpen == prize:
        presenterOpen = random.randrange(1,4)
        
    if choice != prize:
        newchoice = random.randrange(1,4)
        #Ensure the new choice is not the same as the initial choice or the host's door
        while choice == newchoice or newchoice == presenterOpen:
            newchoice = random.randrange(1,4)
            
        if newchoice == prize:
            win += 1
print(str(100*(win/n)) + ' % wins if switch')
