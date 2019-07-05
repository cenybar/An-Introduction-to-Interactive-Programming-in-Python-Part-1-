# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
def name_to_number(name):
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4    
    else: 
        print ("Please type a valid option:rock, Spock, paper, lizard or scissors.")
        return " "    

def number_to_name(number):
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    else: return 'scissors'

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
        
    # print a blank line to separate consecutive games
    print ""
    # print out the message for the player's choice
    print "Player chooses",player_choice
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    import random
    comp_number = random.randrange(0,4)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_name = number_to_name(comp_number)
    # print out the message for computer's choice
    print "Computer chooses",comp_name
    # compute difference of comp_number and player_number modulo five
    modulo_five = (player_number - comp_number) % 5
    # use if/elif/else to determine winner, print winner message
    if modulo_five >= 3:
        print "Computer wins!"
    elif modulo_five >= 1:
        print "Player wins!"
    else:
        print "Player and computer tie!"


    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


