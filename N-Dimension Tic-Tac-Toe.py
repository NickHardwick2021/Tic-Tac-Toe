# FUNCTION NAME: displayBoard
# INPUT: the board
# PROCESS: Put each value on the screen in "tic tac toe" board format
# OUTPUT: The board goes to the output, there is no return value
def displayBoard(board, dimension):
   count = 1
   numx = 0
   for r in range(dimension):
      for c in range(dimension):
         if board[(r*dimension)+c] == '_':
            print("%2d" % count, end = " | ")
         else:
            print("%2.2s" % board[(r*dimension)+c], end= " | ")
         count += 1
      print()

# FUNCTION NAME: filled
# INPUT: the board
# PROCESS: Looks at each spot in the board
# OUTPUT: Return "True" if the board is full, "False" otherwise
def filled (board, dimension):
   for c in board:
      if c == '_':
         return False
      
   return True

# FUNCTION NAME: makeMove
# INPUT: the board, which position to place an "X"
# PROCESS: Checks that the board position is empty; if not, display a message, otherwise update the board
# OUTPUT: No output except perhaps the error message; no return value
def makeMove (board, move, token, dimension):
   if (move<1) or (move>dimension*dimension):
      print("Move is out of range!")
      return False
   if board[move-1] != '_':
      print("That position is filled! Try again!")
      return False
   else:
      board[move-1] = token
      return True

# FUNCTION NAME: fullRow
# INPUT: the board, which player (a character)
# PROCESS: go through each row of the board and see if it is filled with that player marker (character)
# OUTPUT: True if that player marker has filled any row, False otherwise
def fullRow(board, token, dimension):
   for r in range(dimension):
      count = 0
      for c in range(dimension):
         if board[(r*dimension)+c] == token:
            count = count + 1
         if count == dimension:
            return True
      count = 0
         
   return False

# FUNCTION NAME: fullCol
# INPUT: the board, which player (a character)
# PROCESS: go through each column of the board and see if it is filled with that player marker (character)
# OUTPUT: True if that player marker has filled any column, False otherwise
def fullCol(board, token, dimension):
   for x in range (0, dimension):
      count = 0
      for y in range(0, len(board), dimension):
         if board [y+x] == token:
            count += 1
      if count == dimension:
         return True
   return False

# FUNCTION NAME: fullDiag
# INPUT: the board, which player (a character)
# PROCESS: go through each diagonal of the board and see if it is filled with that player marker (character)
# OUTPUT: True if that player marker has filled any diagonal, False otherwise

def fullDiag(board, token, dimension):
   return fullDiag1(board, token, dimension) or fullDiag2(board, token, dimension)

def fullDiag1(board, token, dimension):
   x = 0
   while x < len(board):
      if board[x] != token:
         return False
      x += dimension+1
   return True

def fullDiag2(board, token, dimension):
   x = dimension-1
   while x < len(board)-1:
      if board[x] != token:
         return False
      x += dimension-1
   return True

#FUNCTION NAME: Winner
#Input: board, player (a character) called token
#Process: Check if row, column, or diag for the player
#Output: True if that player maker has filled any row, column or diag, False if else

def winner(board, token, dimension):
   return fullRow(board, token, dimension) or fullCol(board, token, dimension) or fullDiag(board, token, dimension)

#------------------------------------------------
# NEW FUNCTION NAME: winner
# INPUT: the board, the token, the dimension
# PROCESS: Determine if the passed-in token wins the game
# OUTPUT: True if the passed-in-token wins the game, False otherwise
# NEW FUNCTION NAME: move
# INPUT: the board, the token, the dimension
# PROCESS: Make and process the next move
# OUTPUT: The next token (taking turns) AND whether or not the game is ove
def move(board, dimension, token):
    gameOver = False
    displayBoard(board, dimension)
    move = int(input("Enter a move for " + token + " (1-" + str(dimension*dimension) +"): "))
    print(move)
    if (move < 1) or (move > (dimension*dimension)):
        print("Move is out of range; try again.")
    else:
      if makeMove(board, move, token, dimension):
         if winner(board, token, dimension):
            print(token + " wins!")
            gameOver = True
         else:
            if filled(board, dimension):
               print("Board is full! No winner!")
               gameOver = True
            else:
               if token == "X":
                  token = "O"
               else:
                  token = "X"
    return token, gameOver

#Function Name: (New) fillboard
#Input: Board , dimensions
#Process: Fill the board with accurate number of blanks
#Output: The board
def fillBoard(dimension):
   board = []
   for x in range(dimension*dimension):
      board.append('_')
   return board
# END OF FUNCTION DEFINITIONS

# MAIN PART OF THE PROGRAM -- DON'T CHANGE ANYTHING BELOW HERE!

def main():
    print("Play Tic-Tac-Toe!")
    dimension = int(input("What is the dimension of the board (3-12)? "))
    print(dimension)
    if (dimension < 3) or (dimension > 12):
        print("The dimension is out of range")
    else:
        board = fillBoard(dimension)
        token = 'X'
        gameOver = False
        while not gameOver:
            token, gameOver = move(board, dimension, token)
        displayBoard(board, dimension)

if __name__ == "__main__":
    main()