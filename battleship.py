import random
import string
col_size = 9
row_size = 9 

class Board:
    def __init__(self, name):
        self.board = [["."] * 9 for x in range(9)]
        self.ship_locations = []
        self.guesses = []
        self.name = name
        self.shipsDestroyed = 0
        self.addShips()

    def printBoard(self):
        print("\n  " + " ".join(str(x) for x in string.ascii_lowercase[:col_size]))
        for i in range(col_size):
            print(str(i + 1) + " " +" ".join(self.board[i][j] for j in range(row_size)))  
        print()  

    def addShips(self): 
        #sizes=[5,4,3,3,2]
        sizes=[1]
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
        if validCordinates(self,cordinates) == True:
            for cord in cordinates:
                self.board[cord[0]][cord[1]] = "X"
            self.ship_locations.append(cordinates)
            return True     
        else:
            return False

    def attackBoard(self,r,c):
        if self.board[r][c] == "X":
            self.board[r][c] = "*"
            return True
        else:
            return False

class PlayGame:
    def __init__(self,player,rival):
        self.gameOver = False
        self.turns = 0

    def printBoards(self):
        rival.printBoard()
        player.printBoard()

def validCordinates(self,cordinates):
        valid = True
        for cord in cordinates:
            if self.board[cord[0]][cord[1]] == "X":
                 valid = False
        return valid

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
    return c, r

#make this a Board Method (eventually)
def shipSank(board, r,c):
    for ship in board.ship_locations:
        if [r,c] in ship:
            for cord in ship:
                if board.board[cord[0]][cord[1]] != "*":
                    return False
            else:
                return True

player = Board("Daniel")
rival = Board("Computer")

game = PlayGame(player,rival)

def which_turn():
    if game.turns % 2 == 0:
        return player, rival
    else:
        return rival, player

def repeatAttack(attacker,defender):
    while True:
        game.printBoards()

        if attacker == player:
            c, r = selectCoordinates()
        else:
            r,c = random.randint(0,8),random.randint(0,8)
        
        attack_success = defender.attackBoard(r,c)
        if attack_success == True:
            print("{attacker}'s attack was succesful.".format(attacker = attacker.name))

            #Check if the attacked boat has been sanked.
            if shipSank(rival,r,c) == True:
                print("{attacker} sank one of {defender}'s boats!".format(attacker = attacker.name, defender = defender.name))
                attacker.shipsDestroyed += 1

                if attacker.shipsDestroyed == 1:
                    game.gameOver = True
                    break
        else:
            print("{attacker}'s attack missed!\n".format(attacker = attacker.name))
            break

while game.gameOver == False:
    attacker, defender = which_turn()
    repeatAttack(attacker,defender)
    game.turns += 1


    
print("GAME OVER. {attacker} won!".format(attacker = attacker.name))
    


