import random
import string
import time

col_size = 9
row_size = 9 

class Board:
    def __init__(self, name=None):
        self.board = [["."] * 9 for x in range(9)]
        self.rivalBoard = [["."] * 9 for x in range(9)]
        self.ship_locations = []
        self.guesses = []
        self.name = name
        self.shipsDestroyed = 0
        self.addShips()
    
    def addShips(self): 
        sizes=[5,4,3,3,2]
        while sizes:
            valid_slot = self.createShip(sizes[0])
            if valid_slot == True:
                sizes.pop(0)

    def createShip(self,size):
        orientation = 'Horizontal' if random.randint(0,1) == 0 else 'Vertical'
        coordinate1 = random.randint(0,(col_size - 1))
        coordinate2 = random.randint(0,(row_size - size))
       
       #Create a set of cordinates depending the ship's orientation.
        cordinates = [] 
        if orientation == "Horizontal":
            for i in range(size):
                cordinates.append([coordinate1,coordinate2 + i])
        elif orientation == "Vertical":
            for i in range(size):
                cordinates.append([coordinate2 + i,coordinate1])
        
        #Append the ship's cordinates to the ship_locations list attribute if valid.
        if self.validCordinates(cordinates) == True:
            for cord in cordinates:
                self.board[cord[0]][cord[1]] = "X"
            self.ship_locations.append(cordinates)
            return True     
        else:
            return False

    def validCordinates(self,cordinates):
            valid = True
            for cord in cordinates:
                if self.board[cord[0]][cord[1]] == "X":
                    valid = False
            return valid

    def attackBoard(self,r,c):
        if self.board[r][c] == "X":
            self.board[r][c] = "*"
            return True
        else:
            return False

    def shipSank(self, r,c):
        for ship in self.ship_locations:
            if [r,c] in ship:
                for cord in ship:
                    if self.board[cord[0]][cord[1]] != "*":
                        return False
                else:
                    return True

    def printBoard(self,board):
        print("\n  " + " ".join(str(x) for x in string.ascii_lowercase[:col_size]))
        for i in range(col_size):
            print(str(i + 1) + " " +" ".join(board[i][j] for j in range(row_size)))  
        print()  

player = Board()
rival = Board("The Computer")

class PlayGame:
    def __init__(self):
        self.gameOver = False
        self.turns = 0
game = PlayGame()

def printBoards():
    rival.printBoard(rival.rivalBoard)
    player.printBoard(player.board)
    print("-"*42)

def selectCoordinates():
    cordSelected = False   
    while cordSelected == False:
        try:
            print("{player}, enter a coordinate pair, (e.g. 'a4'):".format(player = player.name))
            playerSelection = list(input())
            c = playerSelection[0]
            r = int(playerSelection[1])
        except ValueError:
            print("Invalid option! Select again.")
            continue
        if c in list(string.ascii_lowercase[:9]) and r in range(1,10):    
            c = string.ascii_lowercase.index(playerSelection[0])
            r = int(playerSelection[1]) - 1
            cordSelected == True
            break
        else:
            print("Invalid option! Select again")
    return r, c
def selectRivalCordinates():
    print("{rival} is thinking ".format(rival = rival.name),end="")
    for i in range(4):
        time.sleep(0.4)
        print(".",end="")
    return random.randint(0,8),random.randint(0,8)

def gameLoop(attacker,defender):
    while True:
        printBoards()
        if attacker == player:
            r, c = selectCoordinates()
        else:
            r, c = selectRivalCordinates()
        
        attack_success = defender.attackBoard(r,c)
        if attack_success == True:
            print("\n{attacker}'s attack was succesful.".format(attacker = attacker.name))
            
            if attacker == player:
                rival.rivalBoard[r][c] = "*"

            #Check if the last attack sank a boat.
            if rival.shipSank(r,c) == True:
                print("{attacker} sank one of {defender}'s boats!".format(attacker = attacker.name, defender = defender.name))
                attacker.shipsDestroyed += 1

                #The game loop will end once a player sinks n boats.
                if attacker.shipsDestroyed == 5:
                    game.gameOver = True
                    break
        else:
            print("\n{attacker}'s attack missed!\n".format(attacker = attacker.name))
            break
        
def which_turn():
    if game.turns % 2 == 0:
        return player, rival
    else:
        return rival, player

def printWelcome():
    battleshipTitle = '''
    _           _   _   _           _     _       
    | |         | | | | | |         | |   (_)      
    | |__   __ _| |_| |_| | ___  ___| |__  _ _ __  
    | '_ \ / _` | __| __| |/ _ \/ __| '_ \| | '_ \ 
    | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) |
    |_.__/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/ 
                                            | |    
                                            |_|   '''
    welcome = "Welcome To Ultimate Battleship"
    print(battleshipTitle)
    for i in welcome:
        time.sleep(0.1)
        print(i,end="")
    print("\nEnter your name:")

def playGame():
    printWelcome()
    player.name = input()

    while game.gameOver == False:
        attacker, defender = which_turn()
        gameLoop(attacker,defender)
        game.turns += 1
        
    print("\nGAME OVER. {attacker} won!".format(attacker = attacker.name))
    
def main():
    playGame()

if __name__ == "__main__":
    main()

