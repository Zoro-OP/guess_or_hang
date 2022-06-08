from glob import glob
from itertools import count
from operator import length_hint
import random
from sys import displayhook
import time
from pkg_resources import working_set

from pyparsing import Word

#welcome
print ("Welcome to hangman\n")
name=input("Enter your name: ")
print("Hello "+name +", Best of luck!!!")
time.sleep(2)
print("The game is about to start! Get ready to hang!!!")
time.sleep(3)

#Re execute the game again after the first hang lol!!!
def main():
    global count
    global display
    global Word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage","plants"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""

def play_loop():
    global play_game
    play_game = input("\nDo you wanna hang again xD!!! y = yes, n = no\n")
    while play_game not in ["Y","N","y","n"]:
        play_game = input("Do you wanna hang again XD!!! y = yes, n = no\n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks for hanging by your own choice -_-, We expect you back again to hang lol, HAPPY HANGING")
        exit()

#initializing all the conditions required for the game:
def hangman():
    global count
    global display
    global word 
    global already_guessed
    global play_game
    limit = 5
    guess = input("This is your word: " + display + " Enter your Guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess<="9":
        print("Invalid Input"+name +"Try again -_- !!!\n")
        hangman()
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + guess + display[index + 1:]
        print(display + "\n")
    
    elif guess in already_guessed:
        print("Try another letter.\n")
    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")


            print("Wrong guess. " + str(limit - count) + "Guesses Remaining.\n")
        
        elif count(2):
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            
            print("Wrong Guess. " + str(limit - count) + "Guesses Remaining.\n")
        
        elif count(3):
            time.sleep(1)
            print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")

            print("Wrong guess. " + str(limit - count) + "Guesses Remaining.\n")
        
        elif count(4):
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            
            print("Wrong guess. " + str(limit - count) + "Guess Remaining.\n")
        
        elif count(5):
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")

            print("Wrong guess DUMB, You are hanged. Time to die!!!\n")
            print("The word was: ", already_guessed, word)
            play_loop()

        if word == '_' * length:
            print("OOPS!!! You have guessed the word correctly.\n")
            print(" Anyway, Congratulations!!!\n")
            play_loop()
        elif count != limit:
            hangman()


main()
hangman()