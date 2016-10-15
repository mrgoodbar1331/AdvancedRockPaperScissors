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
2 corresponds to paper, Keyword 2 corresponds to scissors. Do not
let the other player see your keywords. This is the only time that
the players enter their commands in secret. The game then begins.
----------
Player 1 enters his/her choice first, followed by Player 2. If a 
player does not enter one of the three chosen keywords, the game
will randomly choose either rock, paper, or scissors. If the game
has to randomly choose for an individual player more than 3 times,
it will automatically force a loss for that player. If both players
opt for a random choice (or fuck up) and both players are over the
random assignment limit, the game will choose a winner for the round.
----------
The game does not reveal a player's choice. It only reveals the
winner of an individual round. The winner of the previous round goes
first.
----------
After each round, both players have the option to rotate their
keywords. If a player rotates the keywords, then each keyword's
corresponding object is shifted by 1 position. I.E. if keyword 1
was associated with rock, it will be associated with paper after
the rotation.
----------
PROTIP: Don't forget your keywords, the game will not remind you.
----------
PRESS ENTER TO BEGIN
"""

raw_input()

print "Player 1, enter your keywords. (Case and space sensitive) \nPlayer 2, look away."
raw_input("Keyword 1...") = p1k1
raw_input("Keyword 2...") = p1k2
raw_input("Keyword 3...") = p1k3

print "Player 2, enter your keywords. (Case and space sensitive) \nPlayer 1, look away."
raw_input("Keyword 1...") = p2k1
raw_input("Keyword 2...") = p2k2
raw_input("Keyword 3...") = p2k3





















































































