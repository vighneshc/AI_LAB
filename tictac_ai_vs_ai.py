board = [' '] * 9
from time import sleep
import random
def display_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ") 
    print()
display_board(board)
def check_win(agent_mark, board):
    win = [f'{agent_mark}'] * 3
    return board[:3] == win or board[3:6] == win or board[6:9] == win or \
        [board[0], board[4], board[8]] == win or [board[2], board[4], board[6]] == win or \
        [board[0], board[3], board[6]] == win or [board[1], board[4], board[7]] == win or [board[2], board[5], board[8]] == win
def check_draw(board):
    return ' ' not in board
def board_copy(board):
    new_board = []
    for c in board:
        new_board += c
    return new_board
def test_win_move(move, agent_mark, board):
    copy = board_copy(board)
    copy[move] = agent_mark
    return check_win(agent_mark, copy)
def win_strategy(board):
    if board[4] == ' ':
        return 4
    for i in [0, 2, 6, 8]:
        if board[i] == ' ':
            return i
    for i in [1, 3, 5, 7]:
        if board[i] == ' ':
            return i
def get_random():
    return random.randint(0,8)
def get_agent_move(board):
    for i in range(9):
        if board[i] == ' ' and test_win_move(i, 'X', board):
            return i
    for i in range(9):
        if board[i] == ' ' and test_win_move(i, 'O', board):
            return i
    return win_strategy(board)
def tic_tac_toe():
    playing = True
    while playing:
        in_game = True
        first = True
        board = [' ']*9
        while in_game:
            for agent in ['X', 'O']:
                if(first):
                    move = get_random()
                    first = False
                else:
                    move = get_agent_move(board)
                board[move] = agent
                if check_win(agent, board):
                    in_game = False
                    display_board(board)
                    print(f"{agent} won")
                    break
                if check_draw(board):
                    in_game = False
                    display_board(board)
                    print("Its draw!")
                    break
                display_board(board)
                sleep(2)
        print("Continue? y or n")
        ans = input()
        if ans not in 'yY':
            playing = False
tic_tac_toe()
