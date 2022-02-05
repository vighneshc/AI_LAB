import random
import time

def displayBoard(board):
    print('   |   |')
    print(f' {board[7]} | {board[8]} | {board[9]}')
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(f' {board[4]} | {board[5]} | {board[6]}')
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(f' {board[1]} | {board[2]} | {board[3]}')
    print('   |   |')
    
def isFree(pos):
    return board[pos] == ' '


def notFull(board):
    return board.count(' ') > 1


def isWinner(board, ch):
    positions = [[7, 8, 9], [4, 5, 6], [1, 2, 3], [7, 4, 1], [8, 5, 2], [9, 6, 3], [7, 5, 3], [9, 5, 1]]
    win = False
    for i, j, k in positions:
        win |= board[i] == ch and board[j] == ch and board[k] == ch
    return win
def makeMove(board, agent):
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
   
    # Check for possible winning move to take or to block opponents winning move
    agents = ['X', 'O'] if agent == 'X' else ['O', 'X']
    for let in agents:
        for i in possibleMoves:
            boardCopy = board.copy()
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move
    
    random.seed(time.time())
    
    # Try to take Corners
    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    if cornersOpen:
        move = random.sample(cornersOpen, 1)[0]
        return move
   
    # Otherwise Center
    if 5 in possibleMoves:
        move = 5
        return move
 
    # Edges if can't place anywhere else
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
 
    if edgesOpen:
        move = random.sample(edgesOpen, 1)[0]
 
    return move
def main():
    board = [' ' for x in range(10)]
    displayBoard(board)
    
    while notFull(board):
        # Agent 1 ('X')
        move = makeMove(board, 'X')
        board[move] = 'X'
        if move: # Print the board if move is valid ie. not 0 (when board is full)
            print(f"Agent 1 placed 'X' at pos {move}")
            displayBoard(board)
        if isWinner(board, 'X'):
            print("Agent 1 ('X') wins!!!")
            break
        
        # Agent 2 ('O')
        move = makeMove(board, 'O')
        board[move] = 'O'
        if move: # Print the board if move is valid ie. not 0 (when board is full)
            print(f"Agent 2 placed 'O' at pos {move}")
            displayBoard(board)
        if isWinner(board, 'O'):
            print("Agent 2 ('O') wins!!!")
            break
            
        if not move or not notFull(board):
            print("Game is tied")
            break

main()
