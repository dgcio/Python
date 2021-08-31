def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    # TO DO #################################################################
    # Write code in this function that prints the game board.               #
    # The code in this function should only print, the user should NOT      #
    # interact with this function in any way.                               #
    #                                                                       #
    # Hint: you can follow the same process that was done in the textbook.  #
    #########################################################################

def checkWinner(board, player):    
    print('Checking if ' + player + ' is a winner...')

    winner = 0

    WinCombo = [ #winning combos for tic tac toe
                ['top-L', 'top-M', 'top-R'], ['mid-L', 'mid-M', 'mid-R'], ['low-L', 'mid-M', 'low-R'], #vertical
                ['top-L', 'mid-L', 'low-L'], ['top-M', 'mid-M', 'low-M'], ['top-R', 'mid-R', 'low-R'], #horizontal
                ['top-L', 'mid-M', 'low-R'], ['low-L', 'mid-M', 'top-R']] #diagonal

    for x in range(len(WinCombo)): # for loop for the win combos
        winner = 0 #reset the winner counter after every loop
        for y in range(0,3): # for loop for the inner array of winCombo
            print('winner = ' + str(winner)) #debugging
            if board[WinCombo[x][y]] == player: # checks if the current board tarray   equals
                winner += 1 #inc the winner counter
                if winner > 2: #if winner equals two winner has been found
                    return True #return true
                    exit # and exit the program.
        print('----') #debugging

    return False

    # TO DO #################################################################
    # Write code in this function that checks the tic-tac-toe board         #
    # to determine if the player stored in variable 'player' currently      #
    # has a winning position on the board.                                  #
    # This function should return True if the player specified in           #
    # variable 'player' has won. The function should return False           #
    # if the player in the variable 'player' has not won.                   #
    #########################################################################
    
    
def startGame(startingPlayer, board):
    # TO DO #################################################################
    # Add comments to each line in this function to describe what           #
    # is happening. You do not need to modify any of the Python code        #
    #########################################################################

    turn = startingPlayer # detemines who goes first, X or O
    for i in range(9): # begins a for loop with a range of nine
        printBoard(board) # prints the initial board
        print('Turn for ' + turn + '. Move on which space?')
        move = input() # gets the users turn
        board[move] = turn # inserts either X or O depending on whose turn it is
        if( checkWinner(board, 'X') ): # checks if X is the winner
            print('X wins!')
            break
        elif ( checkWinner(board, 'O') ): # checks is ) is the winner
            print('O wins!')
            break
    
        if turn == 'X': # switches the player
            turn = 'O' # if current player is X then switch to O
        else:
            turn = 'X' # else go back to X
        
    printBoard(board) #print the board at its current state
    