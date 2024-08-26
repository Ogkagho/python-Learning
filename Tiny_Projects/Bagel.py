# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 14:25:29 2024

@author: Edward kagho
"""
import random 


def main():
    """
    Displays information about the Game to the the user/

    Returns
    -------
    None.

    """
    print('Bagels, a deductive logic game.')
    print('By Ed. adapted from Al Sweigart')

    print('I am thinking of a 3-digit number. Try to guess what it is.')
    print('Here are some clus: ')
    print('When I say:      That means:')
    print(' Pico            One digit is correct but in the wrong position')
    print(' Fermi           One digit is correct and in the right position.')
    print(' Bagels          No digit is correct')
    
    print('I have thought up a number.')
    print('You have 10 guesses to get it.')
    
def get_clue(guess):
    """
    

    Parameters
    ----------
    guess : string
        Takes guess as a parameter.
        If the player guesses correctly return None, and informs 
        the player they have won.
        if not, returns a clue based on the game specification.

    Returns
    -------
    int.

    """
    if len(guess) < 3 or len(guess) > 3:
        print('The game requires Three digit numbers.')
        return 1
    
    if guess == SECRET_NUM:
        print('Congragulation, You got it')
        return None

    for i in range(3):
        if guess[i] in SECRET_NUM:
            pos = i
            if guess[pos] != SECRET_NUM[pos]:
                print('Pico')
            else:
                print('Fermi')
            return None 
        
    print('Bagels')

def gameStartVar():
    """
    Intitializes varibales needed for the game.
    generates a random 3 digit secret number.
    sets the guess limit
    Returns
    -------
    None.

    """
    global SECRET_NUM, NUM_GUESS_LIMIT, guess
    SECRET_NUM = str(random.randrange(100,1000))
    NUM_GUESS_LIMIT = 10
    guess = 0
    
main()
gameStartVar()

while NUM_GUESS_LIMIT > 0 and guess != SECRET_NUM :
    
    print(f'Guess #{10 - NUM_GUESS_LIMIT + 1}')
    guess = input()

    
    if NUM_GUESS_LIMIT > 1: 
        ans = get_clue(guess)  #get_clue returns a valu if the player enters an inappropriate input
        
    if ans != 1:    #this if accounts for that, not taking away from the playes guess if input is not valid
        NUM_GUESS_LIMIT -= 1  
    
    if NUM_GUESS_LIMIT == 0 or guess == SECRET_NUM:
        if NUM_GUESS_LIMIT == 0:
            print('You lose.')
            print(f'The secret Number was {SECRET_NUM}')
        ans = input('Do you want to play again (yes or no): ')
        if ans.strip().lower() == 'yes':
            gameStartVar() 
        else:
            print('Thank you for Playing. bye ')


        
                    
            
    
