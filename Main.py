"""round robin
tournament bracketing system for MTG draft/sealed:

what is a tournament?
	round robin=everyone fights everyone in a circle
	swiss 	   =forgiving bracket
	bracket    =regular bracket

RR:
	# of players = set beginning; var
	players = class
		names of players = set after #; var
		w/l/d of players = updated matchly; 3 ints
	calculate rand(RR) with player ids
	next pairings = printed at button press
"""
import random


class Player:
    def __init__(self):
        self.name = ""
        self.wins = 0
        self.losses = 0
        self.draws = 0


player_number = int(input("Number of players? "))
players = []
for n in range(player_number):
    players.append(Player())
    players[-1].name = input("Name of player " + str(n) + "? ")
random.shuffle(players)
if player_number % 2 is 1:
    players.append(Player())
    players[-1].name = "Bye"
    player_number += 1
number_matches = player_number-1
print([player.name for player in players])
for match in range(number_matches):
    print("Round", match+1, "Pairings!")
    pairings = []
    for pairing in range(player_number//2-1):
        p1 = (player_number//2 + match - pairing - 1) % (player_number-1)
        p2 = (player_number//2 + match + pairing) % (player_number-1)
        pairings.append((p1, p2))
        print("Pairing", pairing+1, players[p1].name, "vs", players[p2].name)
    if players[-1].name != "Bye":
        pairings.append((-1, match))
    print("Pairing", player_number//2, players[-1].name, "vs", players[match].name)

    entered_pairings = []
    while len(entered_pairings) < len(pairings):
        if len(entered_pairings) == len(pairings)-1:
            for p in range(len(pairings)):
                p += 1
                if p not in entered_pairings:
                    current_input = p
                    break
            print("Automatically Inputting for Pairing", current_input)
        else:
            current_input = int(input("Please Enter Pairing Number "))
            if current_input in entered_pairings:
                print("Bad user, enter an unentered pairing.")
                continue
            elif current_input < 1 or current_input > len(pairings):
                print("Those aren't real numbers??!?!?")
                continue
        entered_pairings.append(current_input)
        current_input -= 1
        wins = int(input("Please input wins for " + players[pairings[current_input][0]].name + " "))
        losses = int(input("Please input losses for " + players[pairings[current_input][0]].name + " "))
        draws = int(input("Please input draws for " + players[pairings[current_input][0]].name + " "))
        players[pairings[current_input][0]].wins += wins
        players[pairings[current_input][0]].losses += losses
        players[pairings[current_input][0]].draws += draws
        players[pairings[current_input][1]].losses += wins
        players[pairings[current_input][1]].wins += losses
        players[pairings[current_input][1]].draws += draws
for player in players:
    if player.name != "Bye":
        print(player.name, player.wins, player.losses, player.draws)
