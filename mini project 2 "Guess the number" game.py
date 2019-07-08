# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables used in your code here

num_range = 100
pending_guesses = 7

# define event handlers for control panel
def range100():
    global num_range
    global pending_guesses
    num_range = 100
    pending_guesses = 7
    new_game()
    
def range1000():
    global num_range
    global pending_guesses
    num_range = 1000
    pending_guesses = 10
    new_game()

# helper function to start and restart the game
def new_game():
    
    global secret_number
    secret_number = random.randrange(0,num_range -1)
    print "New game, range is (0," +str(num_range)+"]"
    print "Number of remaining guesses is " + str(pending_guesses)

    
    
    
def input_guess(guess):
    print "Guess was " + str(guess)
    global pending_guesses
    if pending_guesses == 1:
        print ("Game Over, the number was ") + str(secret_number)
        
    elif int(guess) > secret_number:
        pending_guesses -= 1
        print ("Number of remaining guesses is ") + str(pending_guesses)
        print ("Lower")
    elif int(guess) < secret_number:    
        pending_guesses -= 1
        print ("Number of remaining guesses is ") + str(pending_guesses)
        print ("Higher")    
    else:
        print ("Correct")
    
    

    
# create frame
frame = simplegui.create_frame("Guess the number",200,200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0,100)",range100,200)
frame.add_button("Range is [0,1000)",range1000,200)
frame.add_input("Enter your guess (press enter)",input_guess,200)


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
