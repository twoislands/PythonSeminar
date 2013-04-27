# Rock-paper-scissors-lizard-Spock template
##################################
# SCRIBBLER:	TwoIslandS
# WEBSITE:	http://twoislands.net
# VERSION:	1.0 beta
##################################

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# functions declaration

# name_to_numbers function converts the users choice into
# a number option of the game
def name_to_number(name):
    if name == "rock":
        player_number = 0
    elif name == "Spock":
        player_number = 1
    elif name == "paper":
        player_number = 2
    elif name == "lizard":
        player_number = 3
    elif name == "scissors":
        player_number = 4
    else:
        print "Game Over. Please choose one of the available options"
    return player_number


# number_to_name function converts the 
def number_to_name(number):
    if number == 0
		user_draw = "rock":
	elif number == 1
		user_draw = "spock":
	elif number == 2
		user_draw = "paper":
	elif number == 3
		user_draw = "lizard":
	elif number == 4
		user_draw = "scissors":
	else:
		print "Game Over. Please choose one of the available options"
	return user_draw

def rpsls(name): 
  #
  player_number = name_to_number(name)
  print "Player chooses",name
  #
  comp_number = random.randrange(0, 4)
    print "Computer chooses",number_to_name(comp_number) 
	
  # compute difference of player_number and comp_number modulo five
  if player_number 
  

    # convert name to player_number using name_to_number

    # compute random guess for comp_number using random.randrange()

    

	# use if/elif/else to determine winner

    # convert comp_number to name using number_to_name
    
    # print results
	return

#prints an empty line 
print
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric