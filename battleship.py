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
    def __init__(self):
        self.gameOver = False
        self.turn = None
    
    def printBoards(self,turn):
        printBoard(rival)
        printBoard(player)

        if turn == player:
            print("Enter a coordinate pair, (e.g. 'a4'):")

def printBoard(p):
    print("\n  " + " ".join(str(x) for x in string.ascii_lowercase[:col_size]))
    for i in range(col_size):
        print(str(i + 1) + " " +" ".join(p.board[i][j] for j in range(row_size)))  
    print()  

def validCordinates(self,cordinates):
        valid = True
        for cord in cordinates:
            if self.board[cord[0]][cord[1]] == "X":
                 valid = False
        return valid



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

game = PlayGame()

sanked_ships = 0
while sanked_ships < 5:
    
    attack_success = True
    while attack_success == True:
        
        game.printBoards(player)
        
        guess = list(input())
        c = string.ascii_lowercase.index(guess[0])
        r = int(guess[1]) - 1

        attack_success = rival.attackBoard(r,c)
        
        #Check if guess was successful.
        if attack_success == True:
            print("Your attack was succesful. Strike again.")

            #Check if a boat has been sanked.
            if shipSank(rival,r,c) == True:
                print("You sank a boat!")
                sanked_ships += 1
        else:
            print("You missed!\n")
    
    attack_success = True
    while attack_success == True:
       
        printBoard(rival)
        printBoard(player)
        print("It's the computer's turn.")
        attack_success = player.attackBoard(random.randint(0,8),random.randint(0,8))
        
        if attack_success == True:
            print("The computer's attacks was succesful.\n")
        else:
            print("The computer missed!\n")

print("GAME OVER.")
    

