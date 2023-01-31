#Implementing chess in python
from asyncio.windows_events import NULL
import colorama
from colorama import Fore, Back, Style
#create class for players

class Player():
    def __init__(self, name):
        self.name = name
        self.isWhite = False
        self.noWins = 0
        self.noLoss = 0
        self.graveyard =[]
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.Name = name
        print("Name has been changed to "+name)
    
    def is_white(self):
        return self.isWhite
    
    def set_white(self):
        self.isWhite = True
    

    
#create class for chess board, a matrix containing pieces
class Board():
    def __init__(self):
         #inital board is empty will be set in game class

        #initialise pieces
        #white Pawns
        self.w_pawn1 = Pawn(True,0,6)
        self.w_pawn2 = Pawn(True,1,6)
        self.w_pawn3 = Pawn(True,2,6)
        self.w_pawn4 = Pawn(True,3,6)
        self.w_pawn5 = Pawn(True,4,6)
        self.w_pawn6 = Pawn(True,5,6)
        self.w_pawn7 = Pawn(True,6,6)
        self.w_pawn8 = Pawn(True,7,6)

        #White Rooks
        self.w_rook1= Rook(True,7,7)
        self.w_rook2= Rook(True,0,7)

        #White Knights
        self.w_knight1= Knight(True,6,7)
        self.w_knight2= Knight(True,1,7)

        #White Bishops
        self.w_bishops1= Bishop(True,5,7)
        self.w_bishops2= Bishop(True,2,7)

        #White Queen
        self.w_queen= Queen(True,3,7)

        #White King
        self.w_king= King(True,4,7)

        #black Pawns
        self.b_pawn1 = Pawn(False,0,1)
        self.b_pawn2 = Pawn(False,1,1)
        self.b_pawn3 = Pawn(False,2,1)
        self.b_pawn4 = Pawn(False,3,1)
        self.b_pawn5 = Pawn(False,4,1)
        self.b_pawn6 = Pawn(False,5,1)
        self.b_pawn7 = Pawn(False,6,1)
        self.b_pawn8 = Pawn(False,7,1)
        
        #Black Rooks
        self.b_rook1= Rook(False,7,0)
        self.b_rook2= Rook(False,0,0)

        #Black Knights
        self.b_knight1= Knight(False,6,0)
        self.b_knight2= Knight(False,1,0)

        #Black Bishops
        self.b_bishops1= Bishop(False,5,0)
        self.b_bishops2= Bishop(False,2,0)

        #Black Queen
        self.b_queen= Queen(False,3,0)

        #Black King
        self.b_king= King(False,4,0)

        #All pieces
        self.w_pieces =[self.w_pawn1,self.w_pawn2,self.w_pawn3,self.w_pawn4,self.w_pawn5,self.w_pawn6,
        self.w_pawn7,self.w_pawn8,self.w_rook1,self.w_rook2,self.w_knight1,self.w_knight2,
        self.w_bishops1,self.w_bishops2,self.w_queen,self.w_king]
        
        self.b_pieces = [self.b_pawn1,self.b_pawn2,self.b_pawn3,self.b_pawn4,self.b_pawn5,
        self.b_pawn6,self.b_pawn7,self.b_pawn8,self.b_rook1,self.b_rook2,
        self.b_knight1,self.b_knight2,self.b_bishops1,self.b_bishops2,
        self.b_queen,self.b_king]

        
        self.turn = -1

    def updateboard(self):
        self.pieces = self.w_pieces + self.b_pieces
        self.board = [[None for i in range(8)] for j in range(8)]
        for piece in self.pieces:
            Row = piece.getRow() # row
            Col = piece.getCol() # column

            self.board[Row][Col] = piece
        self.turn +=1
        print(self)
        # board with pieces assigned
    def __str__(self) -> str:
        for row in self.board:
            print(row)
        return ""

    def getBoard(self):
        return(self.board)
    
    def getPiece(self, row, col):
        return self.board[row][col]
    
    def getTurn(self):
        return self.turn
        
        

#create class for chess piece and individual pieces with defined rules
class Piece(): # add pieces can travel through teams pieces
    def __init__(self, white: bool, col_pos, row_pos):
        self.name = None
        self.white = white
        self.row_pos = row_pos
        self.col_pos = col_pos
        return self.name
    def is_valid_move(): #is the move valid
        return False

    def path_clear(self, board:Board, row, col):
        #idea is to get the unit of moves made in a certain direction

        #knight
        if self.name == "knight":
            pass
        #if moving diagonally, bishop
        elif (abs(col - self.col_pos) == abs(row-self.row_pos)):
            row_direction = int(abs(row-self.row_pos)/(row-self.row_pos))
            col_direction = int(abs(col-self.col_pos)/(col-self.col_pos))
            for move in range(1,abs(self.col_pos - col)):
                row_pos = self.row_pos + move*row_direction
                col_pos = self.col_pos + move*col_direction
                if board.getPiece(row_pos,col_pos) != None:
                    return False
            return True

        #if moving horizontal 
        elif self.row_pos - row == 0: # rook or queen or king
            direction = int(abs(self.col_pos - col) / (self.col_pos - col))
            for move in range(1,abs(self.col_pos - col)):
                pos = self.col_pos + move*direction
                if board.getPiece(row,pos) != None:
                    return False
            return True
        #or vertical
        elif self.col_pos - col == 0: #pawn or rook or queen or king
            direction = int(abs(self.row_pos - row) /(self.row_pos - row))
            for move in range(1,abs(self.row_pos - row)):
                pos = self.row_pos + move*-direction
                if board.getPiece(pos,col) != None:
                    return False
            return True
        

    def captured(self, row, col, board:Board):
        if ((board.getPiece(row,col).is_white() == True and self.is_white() == True) 
        or (board.getPiece(row,col).is_white() == False and self.is_white() == False)):
            return False
        pieces = board.b_pieces
        if board.getPiece(row,col).is_white():
            pieces = board.w_pieces
        for piece in pieces:
            if piece == board.getPiece(row,col):
                pieces.remove(piece)
                break
        return True
        #player.graveyard.append(self)


    def is_white(self): #is the piece white
        return self.white
    
    def set_white(self): #get piece to white or it is black by default
        self.white = True
        return self
    
    def getRow(self):
        return self.row_pos
    
    def getCol(self):
        return self.col_pos

    def setRow(self, Row):
        self.row_pos = Row
    
    def setCol(self, Col):
        self.col_pos = Col
    
    def __str__(self) -> str: #print out the piece
        if self.white:
            return "This is a {} it is a white piece, in position: {} , {} ".format(self.name, self.row_pos,self.col_pos)
        return "This is a {} it is a black piece, in position: {} , {} ".format(self.name, self.row_pos,self.col_pos)

    def __repr__(self):
        if not self.is_white():
            return Fore.BLACK + self.name + Fore.RESET
        return Fore.YELLOW + self.name + Fore.RESET

class Pawn(Piece): #Pawn , add promotion in later
    def __init__(self, white: bool, col_pos, row_pos):
        Piece.__init__(self, white, col_pos, row_pos)
        self.name = "Pawn"
        
    def is_valid_move(self, board:Board, end): #is pawn piece moving correctly?
        row = end[0] #row
        col = end[1] #column
        max_row = len(board.getBoard()[0])
        max_col = len(board.getBoard())
        max_move=1
        if self.row_pos == 1 or 6:
            max_move =2

        if self.is_white(): #different for white and black pieces
            max_move = max_move*-1

            if (( col - self.col_pos == 1 and abs(row-self.row_pos) in [-1,1]) and 
                board.getPiece(row,col) != None and 
                row in range(max_row) and col in range(max_col)
                and self.path_clear(board, row, col)): # is there a piece diagonal to it? # capturing the piece
                    return self.captured(row, col, board)

            elif (row >= self.row_pos+max_move  and row < self.row_pos 
            and col == self.col_pos and row in range(max_row) and self.path_clear(board, row, col)): # is it in board range and also only moving one space forward
                if board.getPiece(row,col) == None:
                    return True
                return False
        
        elif not self.is_white(): #different for white and black pieces
            if (row <= self.row_pos+max_move  and row > self.row_pos and col == self.col_pos and row in range(max_row)
            and self.path_clear(board, row, col)): # is it in board range and also only moving one space forward
                if board.getPiece(row,col) == None:
                    return True
                return False
            
            elif (( col - self.col_pos == -1 and abs(row-self.row_pos) in [-1,1])and 
                board.getPiece(row,col) != None and 
                row in range(max_row) and col in range(max_col)
                and self.path_clear(board, row, col)): # is there a piece diagonal to it? # capturing the piece
                    return self.captured(row, col, board)
        return False

class Knight(Piece): #knight piece
    def __init__(self, white: bool, col_pos, row_pos):
        Piece.__init__(self, white, col_pos, row_pos)
        self.name = "Knight"
        
    def is_valid_move(self, board:Board, end): #is Knight piece moving correctly?
        row = end[0]
        col = end[1]
        max_row = len(board.getBoard()[0])
        max_col = len(board.getBoard())
        if (((col == self.col_pos+1 and row == self.row_pos+2)or (col == self.col_pos-1 and row == self.row_pos+2)
        or (col == self.col_pos-1 and row == self.row_pos-2)or (col == self.col_pos+1 and row == self.row_pos-2))
        and row in range(max_row) and col in range(max_col) and self.path_clear(board, row, col)): # is it in board range and also only moving one space forward
            if board.getPiece(row,col) == None:
                return True #move onto empty square
            elif board.getPiece(row,col) != None:
                return self.captured(row, col, board)
        return False

class Rook(Piece): #Rook piece
    def __init__(self, white: bool, col_pos, row_pos):
        Piece.__init__(self, white, col_pos, row_pos)
        self.name = "Rook"
        
    def is_valid_move(self, board:Board, end): #is Rook piece moving correctly?
        row = end[0]
        col = end[1]
        max_row = len(board.getBoard()[0])
        max_col = len(board.getBoard())
        if (((row in range(max_row) and col == self.col_pos)or (col in range(max_col) and row ==self.row_pos))
        and self.path_clear(board, row, col)): # is it in board range and also only moving one space forward
            if board.getPiece(row,col) == None:
                return True
            elif board.getPiece(row,col) !=None:
                return self.captured(row, col, board)
        return False

class Bishop(Piece): #Bishop piece
    def __init__(self, white: bool, col_pos, row_pos):
        Piece.__init__(self, white, col_pos, row_pos)
        self.name = "Bishop"
        
    def is_valid_move(self, board:Board, end): #is Bishop piece moving correctly?
        row = end[0]
        col = end[1]
        max_row = len(board.getBoard()[0])
        max_col = len(board.getBoard())

        if (( abs(col - self.col_pos) == abs(row-self.row_pos)) and row in range(max_row) and col in range(max_col)
        and self.path_clear(board, row, col)): # is it in board range and also only moving one space forward
            if board.getPiece(row,col) == None:
                return True
            elif board.getPiece(row,col) != None:
                return self.captured(row, col, board)
        return False

class King(Piece): #King piece, need to edit, can move one pos in any direction
    def __init__(self, white: bool, col_pos, row_pos):
        Piece.__init__(self, white, col_pos, row_pos)
        self.name = "king"
    
    def is_trapped(self, board:Board):
        #the moves the king can make
        movelist =[[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
        #king_valid_move = all([self.is_valid_move(move) for move in movelist]) 
        pieces = board.w_pieces
        if self.is_white():
            pieces = board.b_pieces
        for piece in pieces:
            print(piece)
            if piece.path_clear(board, self.row_pos, self.col_pos) != True:
                print(piece.path_clear(board, self.row_pos, self.col_pos))
                if type(piece.path_clear(board, self.row_pos, self.col_pos)[1]) == King():
                 print("trapped")
                 return 
                


    def is_valid_move(self, board:Board, end): #is king piece moving correctly?
        row = end[0]
        col = end[1]
        max_row = len(board.getBoard()[0])
        max_col = len(board.getBoard())

        if ((abs(row - self.row_pos) <= 1) and abs(col - self.col_pos) <=1 
        and row in range(max_row) and col in range(max_col)
        and self.path_clear(board, row, col)): # is it in board range and also only moving one space forward
            if board.getPiece(row,col) == None:
                return True
            elif board.getPiece(row,col) != None:
                return self.captured(row, col, board)
        return False

class Queen(Piece): #Queen piece
    def __init__(self, white: bool, col_pos, row_pos):
        Piece.__init__(self, white, col_pos, row_pos)
        self.name = "Queen"
        
    def is_valid_move(self, board: Board, end): #is Queen piece moving correctly?
        row = end[0]
        col = end[1]
        max_row = len(board.getBoard()[0])
        max_col = len(board.getBoard())

        if ((( abs(col - self.col_pos) == abs(row-self.row_pos) and row in range(max_row) and col in range(max_col)) # is it in board range and also only moving one space forward
            or ((row in range(max_row) and col == self.col_pos)or (col in range(max_col) and row ==self.row_pos)))
            and self.path_clear(board, row, col)):
            if board.getPiece(row,col) == None:
                return True
            elif board.getPiece(row,col) != None:
                return self.captured(row, col, board)
        return False
#create class for a game/chess
class Chess():
    def __init__(self):
        self.board = None
        self.player_1 = None
        self.player_2 = None
        self.state = None
    
    def get_state(self):
        return self.state

    def set_state(self, new_state):
        if new_state.lower() in ["start", "playing", "end"]:
            self.state = new_state.lower()
        else:
            print("Invalid State")
    
    def select_colour(self, player1: Player, player2: Player):
        #could be random but for now set player1 to white and player2 to black
        player1.set_white() # player remains black
    
    def runState(self):
        #if None then initialise the board and configure a game
        if self.state == None:
            print("Starting Chess game")
            #get the players names
            player1 = input("Please Enter the name of the first player: ")
            player2 = input("Please Enter the name of the second player: ")

            self.player_1 = Player(player1)
            self.player_2 = Player(player2)

            #select colour
            self.select_colour(self.player_1, self.player_2)

            #create the board and initialise pieces
            self.board = Board()

            #game created switch state to playing  
            self.set_state("playing")
            self.board.updateboard()
            self.runState()

        elif self.state == "playing":
            print("playing")
            #get the players move
            if self.board.getTurn() % 2 != 0:
                print(("{}'s Turn").format(self.player_2.get_name()))
                #if self.board.getTurn() > 1:
                #    self.board.b_king.is_trapped(self.board)
            else:
                print(("{}'s Turn").format(self.player_1.get_name()))
                #if self.board.getTurn() > 1:
                #    self.board.w_king.is_trapped(self.board)
            #get the piece that they would like to move, maybe even highlight it
            start = input("Please enter the position of the piece, [Row, Col]: ")
            #get the position they would like to move to
            end = input("Please enter the position you want to move the piece to, [Row, Col]: ")

            self.makeMove([int(start[1]),int(start[3])],[int(end[1]),int(end[3])])
            self.runState()
        elif self.state == "end":
            print("Game Finished")
            pass
        else:
            print("Invalid State")

            #assign a colour to the players
    def set_move(self, piece, End, row2,col2):
        if piece.is_valid_move(self.board, End):
            piece.setRow(row2)
            piece.setCol(col2)
            print("moved")
            return self.board.updateboard()
        print("Invalid Move")
        

    def makeMove(self, Start: list, End: list):
        #select piece to move
        row1 = Start[0] # row
        col1 = Start[1] # column
        row2 = End[0] # row
        col2 = End[1] # column
        piece = self.board.getPiece(row1,col1)
        if piece == None:
            print("Empty Spot")
            return
        if self.board.getTurn() % 2 == 0 and piece.is_white():
            self.set_move(piece, End, row2, col2)
            return
        elif self.board.getTurn() % 2 != 0 and not piece.is_white():
            self.set_move(piece, End, row2, col2)
            return
        print("Invalid Piece")
        return
    
    

#main program

def main():
    game = Chess()
    game.runState()
    pass

if __name__ == '__main__':
    main()

#in chess when move is approved in Piece then run it from chess class.
# or run directly from the valid checker
#main chess will ask for current piece location

#testing Pieces
#ChessBoard = Board()
#player1 = Player("Tobi")
#player2 = Player("Bot")
#Game = Chess(ChessBoard, player1, player2)

#P_pawn = Pawn(True,0,0)
#P_knight = Knight(True,0,0)
#P_rook = Rook(True,0,0)
#P_bishop = Bishop(True,0,0)
#P_Queen = Queen(True,0,0)
#P_King = King(True,0,0)
#print(P_pawn.is_valid_move(ChessBoard, [0,0]))
#print(P_knight.is_valid_move(ChessBoard, [1,2]))
#print(P_rook.is_valid_move(ChessBoard, [5,2]))
#print(P_bishop.is_valid_move(ChessBoard, [0,0]))
#print(P_Queen.is_valid_move(ChessBoard, [0,7]))
#print(P_King.is_valid_move(ChessBoard, [1,1]))

#ChessBoard.updateboard()
#Game.makeMove([6,0],[4,0])
#Game.makeMove([1,1],[3,1])
#Game.makeMove([4,0],[3,0])
#Game.makeMove([1,0],[2,0])

#print(ChessBoard)


