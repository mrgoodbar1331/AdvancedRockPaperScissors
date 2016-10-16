#This is important: version 2.7.12

import random


print """WELCOME TO ROCK, PAPER, SCISSORS: ADVANCED
-----------
This game is a turn based version of rock, paper, scissors.
Obviously, you both are sitting right next to each other, so
there are built in mechanisms to drastically increase the 
difficulty, and thus, the skillcap.
-----------
WIN CONDITIONS: First to seven.
-----------
PRESS ENTER TO PLAY
"""

raw_input()

print """INSTRUCTIONS
----------
This will only be presented once, pay attention! The game will
ask you for your keywords. Keyword 1 corresponds to rock, keyword
2 corresponds to paper, Keyword 3 corresponds to scissors. Do not
let the other player see your keywords. This is the only time that
the players enter their commands in secret. The game then begins.
----------
Player 1 enters his/her choice first, followed by Player 2. If a 
player does not enter one of the three chosen keywords, the game
will randomly choose either rock, paper, or scissors. If the game
has to randomly choose for an individual player more than 3 times,
that player will automatically lose the round. If both players
opt for a random choice (or messes up) and both players are over the
random assignment limit, the game will choose a winner for the round.
----------
The game does not reveal a player's choice. It only reveals the
winner of an individual round. The winner of the previous round goes
first.
----------
After each round, the losing player has the option to rotate their
keywords. If a player rotates the keywords, then each keyword's
corresponding object is shifted by 1 position. I.E. if keyword 1
was associated with rock, it will be associated with paper after
the rotation.
----------
PROTIP: Don't forget your keywords, the game will not remind you.
PROTIP: There are no do-overs, don't fuck up.
PROTIP: Each player should use a pen and pad; the game is trickier
than you think.
----------
PRESS ENTER TO BEGIN
"""

raw_input()

print "Player 1, enter your keywords. (Case and space sensitive) \nPlayer 2, look away.\n"
p1k1 = raw_input("Keyword 1: ")
p1k2 = raw_input("Keyword 2: ")
p1k3 = raw_input("Keyword 3: ")
print "Press ENTER to continue."
raw_input()

print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

print "Player 2, enter your keywords. (Case and space sensitive) \nPlayer 1, look away.\n"
p2k1 = raw_input("Keyword 1: ")
p2k2 = raw_input("Keyword 2: ")
p2k3 = raw_input("Keyword 3: ")
print "Press ENTER to continue."
raw_input()

print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"


p2wins = False
#This is how we will make the winner go first.

p1randomcount = 0
p2randomcount = 0
#This is how we keep track of the random count.

p1score = 0
p2score = 0
#This is how we will keep score

#IMPORTANT: i messed up and used the actual variable names as the parameters for these functions,
#it made things very confusing (for like 15 min). I suggest to not do that, lol


def rotate(p1k1, p1k2, p1k3, p2k1, p2k2, p2k3, p2wins):
#So with this function i discover that i have to give a function all the values that
#i want it to use. i would have structured this whole game differently had
#i known that fact before starting.
	if p2wins == False:
		print "Player 2, would you like to rotate your keywords? y/n "
		z = raw_input()
		if z == "y" or z == "Y":
			print "Rotating player 2 keywords."
			# I have to have an intermediate step when switching the keywords 
			# or the logic kinda just... fails.
			first = p2k1
			second = p2k2
			third = p2k3
			p2k2 = first
			p2k3 = second
			p2k1 = third
			print "Keywords have been rotated."
		else:
			print "Your keywords will not be rotated."
	else:
		print "Player 1, would you like to rotate your keywords? y/n "
		z = raw_input()
		if z == "y" or z == "Y":
			print "Rotating player 1 keywords."
			first = p1k1
			second = p1k2
			third = p1k3
			p1k2 = first
			p1k3 = second
			p1k1 = third
			print "Keywords have been rotated."
		else:
			print "Your keywords will not be rotated."
	return p1k1 , p1k2, p1k3, p2k1, p2k2, p2k3

def thegame(p2wins , p1score , p2score , p1randomcount , p2randomcount):
#I'm not sure if this is the most efficient way, but it works.
	drawstatement = "This round is a draw!\n"
	#using variables for the victorystatements was sooooo clutch, I just saved myself
	#like 20 min of mindless editing.
	p1victorystatement = "Player 1 wins this round!\n"
	p2victorystatement = "Player 2 wins this round!\n"
	print "Press ENTER to begin the round."
	raw_input()
	if p2wins == True:
		p2c = raw_input("Player 2 choice: ")
		p1c = raw_input("Player 1 choice: ")
	else:
		p1c = raw_input("Player 1 choice: ")
		p2c = raw_input("Player 2 choice: ")

	if p1c == p1k1 and p2c == p2k1:
		print drawstatement
	elif p1c == p1k1 and p2c == p2k2:
		print p2victorystatement
		p2score += 1
		p2wins = True
	elif p1c == p1k1 and p2c == p2k3:
		print p1victorystatement
		p1score += 1
		p2wins = False
	elif p1c == p1k2 and p2c == p2k1:
		print p1victorystatement
		p1score += 1
		p2wins = False
	elif p1c == p1k2 and p2c == p2k2:
		print drawstatement
	elif p1c == p1k2 and p2c == p2k3:
		print p2victorystatement
		p2score += 1
		p2wins = True
	elif p1c == p1k3 and p2c == p2k1:
		print p2victorystatement
		p2score += 1
		p2wins = True
	elif p1c == p1k3 and p2c == p2k2:
		print p1victorystatement
		p1score += 1
		p2wins = False
	elif p1c == p1k3 and p2c == p2k3:
		print drawstatement
#This is where it gets tricky
#This part runs if p2 does not choose keyword and p1 does
	#NOTE: The random function parameters are (start, stop, step)
	#it includes the start, but excludes the stop in the possible choices
	#this means it can only ever be 1 or 2, so its not possible to draw
	#if a player decides to not enter a keyword
	elif p1c == p1k1 or p1c == p1k2 or p1c == p1k3:
		if p2randomcount < 3:
			n = random.randrange(1 , 3 , 1)
			p2randomcount += 1
			if n == 1:
				print p1victorystatement
				p1score += 1
				p2wins = False
			elif n == 2:
				print p2victorystatement
				p2score += 1
				p2wins = True
			else:
				print drawstatement
		else:
			print p1victorystatement
			p1score += 1
			p2wins = False
	#This part runs if p1 does not choose keyword and p2 does
	elif p2c == p2k1 or p2c == p2k2 or p2c == p2k3:
		if p1randomcount < 3:
			n = random.randrange(1 , 3 , 1)
			p1randomcount += 1
			if n == 1:
				print p1victorystatement
				p1score += 1
				p2wins = False
			elif n == 2:
				print p2victorystatement
				p2score += 1
				p2wins = True
			else:
				print drawstatement
		else:
			print p2victorystatement
			p2score += 1
			p2wins = True
	#This part runs if both players do not choose a keyword
	else:
		if p1randomcount > 2 and p2randomcount > 2:
			n = random.randrange(1 , 3 , 1)
			if n == 1:
				print p1victorystatement
				p1score += 1
				p2wins = False
			elif n == 2:
				print p2victorystatement
				p2score += 1
				p2wins = True
			else:
				print drawstatement
		elif p1randomcount > 2:
			p2randomcount += 1
			print p2victorystatement
			p2score += 1
			p2wins = True
		elif p2randomcount > 2:
			p1randomcount += 1
			print p1victorystatement
			p1score += 1
			p2wins = False
		else:
			p1randomcount += 1
			p2randomcount += 1
			n = random.randrange(1 , 3 , 1)
			if n == 1:
				p1score += 1
				print p1victorystatement
				p2wins = False
			elif n == 2:
				p2score += 1
				print p2victorystatement
				p2wins = True
			else:
				print drawstatement
	return p2wins , p1score , p2score , p1randomcount , p2randomcount


while p1score < 7 and p2score < 7:
#fun little tidbit: at a point while testing the program wouldn't ever run the game.
#after spending hours looking for the error (jk it only took 10 sec, that was for dramatic effect)
#i discovered that i had "greater than" signs instead of "less than" signs
#funny how the difference between a broken program and a working program could be
#which way the carrots point.				
	p2wins , p1score , p2score , p1randomcount , p2randomcount = thegame(p2wins , p1score , p2score , p1randomcount , p2randomcount)
	print "Player 1 score: ", p1score
	print "Player 2 score: ", p2score, "\n"
	print p1randomcount , p2randomcount
	p1k1, p1k2, p1k3, p2k1, p2k2, p2k3 = rotate(p1k1, p1k2, p1k3, p2k1, p2k2, p2k3, p2wins)
	#I feel so bad for having to pass 7 parameters to that function, lol
	
if p1score == 7:
	print "Congrats Player 1, you just used your raw brain power to destroy player 2!"
if p2score == 7:
	print "Congrats Player 2, you just intellectually dominated player 1!"
	
# bois, i just wrote that like it was nothing
	

	
	
	
print p2wins
print p1score
print p2score
print p1randomcount
print p2randomcount
				
#add rotate feature
#add several rounds instead of 1
#extend white space between keyword entry
#add statements that show score at end of each round
#import randompy
				
		
		
		
#WHOA, IT'S DONE AND IT WORKS!!!!!!!!!!!!!!!!!!!!!!!!!!
	
	






















































































