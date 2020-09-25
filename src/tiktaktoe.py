import numpy as np
def printBoard(contents): #contens has to be a list of 9 elements 
    if len(contents) > 9 or len(contents) < 9:
        return
    s = ""
    num = 0
    while num < 9:
        s += str(contents[num])
        if (num +1) % 3 == 0: 
            s += "\n"
            if num < 8:
                s+= "------\n"
        else:
            s += '|'
        num += 1
    print(s)

def has_won(player, contents): # X or O
    if player.lower() != "x" and player.lower() != "o":
        return False
    num = 0
    won = 0
    while num < 9:
        if contents[num] == player:
            won += 1
        if (num + 1) % 3 == 0 and won == 3:
            return True
        num += 1
    
    #reset that shit
    num = 0
    won = 0
    rounds = 0
    while rounds < 3:
        while num < 9:
            if contents[num] == player:
                won += 1
            num += 3
        if won == 3:
            return True
        num -= 8
        won = 0
        rounds += 1
    return ((contents[0] == player and contents[8] == player) or (contents[2] == player and contents[6] == player)) and contents[4] == player

def is_tie(contents):
    for s in contents:
        if s == ' ':
            return False
    return True

def make_turn(player, contents):
    pl_input = "no"
    s = ""
    while len(pl_input) < 3 and not "," in pl_input:
        print(f"Player {player} >")
        pl_input = input()
        print(pl_input)
    pl_input.replace(' ','')
    s = pl_input.split(',')
    i = 0
    while i < len(s):
        s[i] = int(s[i])
        i += 1
    
    val = int(s[0] -1) + int((s[1] -1) * 3)
    if contents[val] == ' ':
        contents[val] = player
    
    if has_won(player,contents) == True:
        print(f"Player {player} has won!")
        return True
    elif is_tie(contents) == True:
        print("It's a tie!")
        return True
    return False

def reset_contents(contents):
    for i in range(len(contents)):
        contents[i] = ' '
    return contents

import sys
print("Welcome to TikTakToe by PinPhreek!")
players = ['X', 'O']
pl_input = ""
contents = [1,2,3,4,5,6,7,8,9]
contents = reset_contents(contents)
while True:
    while True:
        print("Type \'Start\' to start and \'End\' to end")
        pl_input = input()
        if pl_input.lower() == "start":
            break
        elif pl_input.lower() == "end":
            sys.exit()
        else:
            print(f" {pl_input} is not a valid command!")
    while True:
        printBoard(contents)
        if make_turn(players[0],contents) == True:
            print("Play again?")
            pl_input = input()
            if "n" in pl_input.lower():
                sys.exit()
            break
        printBoard(contents)
        if make_turn(players[1], contents) == True:
            print("Play again?")
            pl_input = input()
            if "n" in pl_input.lower():
                sys.exit()
            break
    