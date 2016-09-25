import random

def print_board(board):
    for i in range(9):
        print(board[i] + '|', end='')
        if (i + 1) % 3 == 0:
            print('\b ')

def check_win(board, symbol):
    win_conditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in win_conditions:
        if board[i[0]] == board[i[1]] and board[i[1]] == board[i[2]] and board[i[0]] == symbol:
            return True
    return False

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
turn = 1
player1_symbol = input('Enter the symbol player 1 \'X\' or \'O\': ')
player2_symbol = 'O'
if player1_symbol == 'O':
    player2_symbol = 'X'
while turn <= 10:
    print_board(board)
    if check_win(board, player1_symbol) == True:
        print('Player 1 won!')
        break;
    elif check_win(board, player2_symbol) == True:
        print('Player 2 won!')
        break;
    elif turn == 10:
        print('Draw')
        break;
    else:
        if turn % 2 == 0:
            move = int(input('Player 2 move (1-9): ')) - 1
            if board[move] == ' ':
                board[move] = player2_symbol
                turn += 1
            else:
                print('Enter a blank square')
        else:
            move = int(input('Player 1 move (1-9): ')) - 1
            if board[move] == ' ':
                board[move] = player1_symbol
                turn += 1
            else:
                print('Enter a blank sqaure')

'''
##############
#   OUTPUT   #
##############
Enter the symbol player 1 'X' or 'O': X
 | |
 | |
 | |
Player 1 move (1-9): 5
 | |
 |X|
 | |
Player 2 move (1-9): 2
 |O|
 |X|
 | |
Player 1 move (1-9): 1
X|O|
 |X|
 | |
Player 2 move (1-9): 9
X|O|
 |X|
 | |O
Player 1 move (1-9): 7
X|O|
 |X|
X| |O
Player 2 move (1-9): 4
X|O|
O|X|
X| |O
Player 1 move (1-9): 3
X|O|X
O|X|
X| |O
Player 1 won!
'''
