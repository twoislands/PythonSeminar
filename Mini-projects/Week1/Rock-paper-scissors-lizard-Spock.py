"""
Rock-paper-scissors-lizard-Spock template
-----------------------------------------
SCRIBBLER:	TwoIslandS
WEBSITE:	http://twoislands.net
VERSION:	0.3 beta
-----------------------------------------
The key idea of this program is to equate the strings
"rock", "paper", "scissors", "lizard", "Spock" to numbers
as follows:

# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
"""

# LIBRARIES
import random

# FUNCTIONS
def name_to_number(guess):
    #name_to_numbers function converts the users choice into
    #a number option of the game
    if guess == "rock":
        player_number = 0
    elif guess == "Spock":
        player_number = 1
    elif guess == "paper":
        player_number = 2
    elif guess == "lizard":
        player_number = 3
    elif guess == "scissors":
        player_number = 4
    else:
        print "Game Over. Please choose one of the available options"
    return player_number

def number_to_name(number):
    #number_to_name function assigns one of game's option
    #to the random generated number
    if number == 0:
        user_draw = "rock"
    elif number == 1:
        user_draw = "spock"
    elif number == 2:
        user_draw = "paper"
    elif number == 3:
        user_draw = "lizard"
    elif number == 4:
        user_draw = "scissors"
    else:
        print "Game Over. Please choose one of the available options"
    return user_draw

def rpsls(name):
    #rpsls fuction will choose the winner based on 
    #Rock-paper-scissors-lizard-Spock rules
    player_number = name_to_number(name)
    print "Player chooses",name
  
    comp_number = random.randrange(0, 5)
    print "Computer chooses",number_to_name(comp_number)
    
    winner = player_number - comp_number
    #if the number is below zero it will add 5 
    #(as 0-1-2-3-4 are 5 numbers) to convert it to positive number
    if (winner < 0):
        winner +=5
    
    #The following if-statement will decide who wins.
    if (winner == 1) or (winner == 2):
        print "Player wins!"
    elif (winner == 3) or (winner == 4):
        print "Computer wins!"
    else:
        print "Player and computer tie!"
    return
    
# CODE-TEST
rpsls("rock")
print ""
rpsls("Spock")
print ""
rpsls("paper")
print ""
rpsls("lizard")
print ""
rpsls("scissors")
print ""
print "Game is Over. Good Bye"
# always remember to check your completed program against the grading rubric

#http://www.codeskulptor.org/#user10_TqBlK70zXW6ZPgi.py
