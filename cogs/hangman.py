###############################################################################################################
# Author: Scott Neaves 09/08/2015                                                                             #   
# Hangman                                                                                                     #
# Python v2.7                                                                                                 #
###############################################################################################################

from random import choice
import string
import webbrowser

dictionary = ['horseradish', 'juggler', 'banana', 'black', 'why', 'until', 'serendipitous', 'extraneous', 'phenomenal', 'iridescent', 'opalescent', 'dictionary', 'difficult'] 
continue_play = True

while continue_play==True:
    #region initialization              
    win = False
    strikes = []
    guesses = []    
    word = list(choice(dictionary))
    display_word = len(word)*['*']  
    print("\nLet's play HANGMAN! Can you guess the word in 7 strikes?")
    print("".join(display_word) + "\n")
    #endregion

    #region game loop
    while (win == False and len(strikes) < 7):
        letter = raw_input("Guess a letter! ").lower()

        if not letter in string.ascii_lowercase or letter=='':
            continue

        if letter in guesses:
            print ('\nYou already guessed that one, please try again.')
        else: 
            guesses += [letter]
            if letter in word:
                print("\nCorrect Guess!")
                for x in range(0, len(word)):
                    if letter == word[x]:
                        display_word[x] = word[x]
            else:
                strikes += [letter]
                print("\nIncorrect Guess.")

        print("The mystery word so far:", "".join(display_word))
        print("Letters you have already guessed:", guesses)
        print("Strikes remaining: " + str(7-len(strikes)) + "\n")

        if display_word == word:
            win = True
    #endregion

    if win == True:
        print("\nHats off to you! You win!")
    else:
        print("\nYou lost this time. Can't win 'em all.")
    print("The word was '", ''.join(word) , "'")


    while True:
        inpt = raw_input("\nWould you like to play again? Y for yes, N for no, or press S to share your " + ("success" if win else "regretful failure") + " on teh interwebs!")
        if inpt in ['N', 'n']:
            continue_play = False
            break
        elif inpt in ['Y', 'y']:
            break
        elif inpt in ['S', 's']:
            webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ', 2, True)
            continue_play = False
            break
        else:
            continue