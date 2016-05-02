#Hangman
# ------------------------------------------
#                                           |
#                                           |
#               HANGMAN                     |
#       Created by Frogsicle in 2016        |
#                                           |
#                                           |
# ------------------------------------------
#!/usr/bin/env python3
import time
import os
from turtle import *
move = Turtle()
import sys



#(Clears the screen)
def cls():os.system("cls")

#Leaves a line blank
def blank():print(" ")

# Creates a line accross the terminal
def line():
    print("_________________________________________________________________")

# Pauses the terminal using the system command 'pause'. The nul section of the command makes it silent and not display press any key to continue text
def pause():
    os.system("pause >nul")

# The section of the game where the word is chosen.
# This function is called by the guess() function when it runs.
# It returns the word chosen by player 1 when called.
def startup():
    blank()
    line()
    blank()
    print("HANGMAN")
    blank()
    print("Player 1 enter word for Player 2 to guess. All letters must be lower-case.")
    word = input(">>>")
    # Easter egg to draw the full hangman if the string 'drawHangman' is used as a word. I was bored
    if word == "drawHangman":
        wrong(1)
        wrong(2)
        wrong(3)
        wrong(4)
        wrong(5)
        wrong(6)
        wrong(7)
        wrong(8)
        wrong(9)
        wrong(10)
        pause()
        sys.exit(0)
    cls()
    print("Pass the device to Player2...")
    time.sleep(3)
    cls()
    return word


#This function draws the hangman using turtle graphics
def wrong(guessNumber):
    speed(0)
    if guessNumber == 1:
        move.left(180)
        move.forward(100)
        move.left(180)
        move.forward(50)
    elif guessNumber == 2:
        move.left(90)
        move.forward(100)
    elif guessNumber == 3:
        move.right(90)
        move.forward(100)
    elif guessNumber == 4:
        move.left(180)
        move.forward(75)
        move.left(45)
        move.setposition(-50, 75)
    elif guessNumber == 5:
        move.penup()
        move.setposition(50, 100)
        move.pendown()
        move.setposition(50, 80)
        move.left(45)
    elif guessNumber == 6:
        move.right(90)
        move.circle(10)
        move.penup()
        move.setposition(50, 60)
    elif guessNumber == 7:
        move.left(90)
        move.pendown()
        move.forward(30)
        move.left(180)
        move.forward(15)
    elif guessNumber == 8:
        move.left(90)
        move.forward(10)
        move.left(180)
        move.forward(20)
        move.left(180)
        move.penup()
    elif guessNumber == 9:
        move.setposition(50, 30)
        move.pendown()
        move.left(45)
        move.forward(20)
    elif guessNumber == 10:
        move.setposition(50, 30)
        move.left(90)
        move.forward(20)
def guess():
    word = startup()
    wordLength = len(word)
    correctChars = ""
    counter = 0
    guess = ""
    wrongCounter = 0
    correctCounter = 0
    while True:
        cls()

        blank()
        line()
        blank()
        print("HANGMAN")
        blank()
        print("Your word has " + str(wordLength) + " letters")
        charsToBeAdded = ""
        for character in word:

            counter = counter + 1
            if character in correctChars:
                print(character)
            elif character == guess:
                print(character)
                correctCounter = correctCounter + 1
                charsToBeAdded = charsToBeAdded + character

            else:
                print("___")
        correctChars = correctChars + charsToBeAdded
        print("You have incorrectly guessed " + str(wrongCounter) + " times")
        if correctCounter == wordLength:
            break
        blank()
        print("Awaiting Guess Player 2")
        guess = input(">>>")
        if guess == word:
            break
        if guess not in word:
            move.hideturtle()
            speed(0)
            wrongCounter = wrongCounter + 1
            wrong(wrongCounter)
        if wrongCounter == 10:
            cls()
            print("You entered too many incorrect guesses. Player 1 wins!")
            time.sleep(3)
            sys.exit(0)








guess()
cls()
print("You got the word correct!")
blank()
time.sleep(1)

pause()
