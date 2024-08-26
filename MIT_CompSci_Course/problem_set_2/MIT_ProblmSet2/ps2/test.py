import os
import sys

# Change the working directory to the folder containing your files
os.chdir('C:\\Users\\Lenovo\\Desktop\\Programming CS\\Python_projects_exercises\\MIT_CompSci_Course\\problem_set_2\\MIT_ProblmSet2\\ps2')

# Add the directory to the system path
sys.path.append(os.getcwd())

import hangman

# Load the word list once
wordlist = hangman.load_words()

# Choose a word from the loaded word list
word = hangman.choose_word(wordlist)
num_guesses = 6

print('Welcome to the game of Hangman!')
lenword = len(word)
print(f'I am thinking of a word that is {lenword} letters long.')
print('-----------')
print(f'You have {num_guesses} guesses left')
letters_guessed = []
print('Available letters: ' + hangman.get_available_letters(letters_guessed))

while num_guesses > 0:
    letters_guessed += input('Enter guess: ')
    if hangman.is_word_guessed(word, [letters_guessed[-1]]):
        print('Good guess: ' + hangman.get_guessed_word(word, letters_guessed))
    else:
        print('Oops! That letter is not in my word: ' + hangman.get_guessed_word(word, letters_guessed))
        num_guesses -= 1
    print('----------')
    print(f'You have {num_guesses} guesses left')
    print('Available letters: ' + hangman.get_available_letters(letters_guessed))

