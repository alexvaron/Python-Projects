# Created by Alex Varon on 1/3/21.

#import time
import time

#welcome user
name = input("What is your name? ")

print ("Hi " + name, "I challenge you to a game of hangman!")

#wait 1 second
time.sleep(1)

print ("Start guessing...")

#wait .5 second
time.sleep(0.5)

#hardcoding the word as hangman
word = "hangman"

#creates a variable with the number of guesses
guesses = ''
#number of turns
turns = 10

while turns > 0: #iff turns more than zero
    failed = 0 #counter

    for char in word: #iterate through word
        if char in guesses:
            print (char)
        else:
            print ("_")# if not found, print a dash
            
            failed += 1
    if failed == 0: #user wins
        print ("You won")
        break
    print
    
    guess = input("guess a letter:")
    guesses += guess
    if guess not in word: #guesses incorrectly
        turns -= 1
        print ("Incorrect")
        print ("You have", + turns, 'more guesses')
        
        if turns == 0:
            print ("I win again!")
