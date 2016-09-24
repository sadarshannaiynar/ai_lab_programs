import random

def print_board(board):
    for i in range(9):
        print(board[i] + '|', end='')
        if (i + 1) % 3 == 0:
            print('\b ')

def decide_move(board, val):
    win_conditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in win_conditions:
        if board[i[0]] == board[i[1]] and board[i[0]] == val and board[i[2]] == ' ':
            return i[2]
        elif board[i[1]] == board[i[2]] and board[i[1]] == val and board[i[0]] == ' ':
            return i[0]
        elif board[i[0]] == board[i[2]] and board[i[2]] == val and board[i[1]] == ' ':
            return i[1]
    return -1;

def check_free(board):
    i = random.randrange(0, 8)
    if board[i] != ' ':
       return check_free(board)
    else:
        return i

def make_move(board, user_symbol, computer_symbol):
    win_move = decide_move(board, computer_symbol)
    if win_move == -1:
        block_move = decide_move(board, user_symbol)
        if block_move == -1:
            return check_free(board)
        return block_move
    return win_move

def check_win(board, symbol):
    win_conditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in win_conditions:
        if board[i[0]] == board[i[1]] and board[i[1]] == board[i[2]] and board[i[0]] == symbol:
            return True
    return False

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
turn = 1
user_symbol = input('Enter your symbol X or O: ')
computer_symbol = 'O'
if user_symbol == 'O':
    computer_symbol = 'X'
while turn <= 10:
    print_board(board)
    if check_win(board, 'O') == True:
        print('The computer won!')
        break;
    elif check_win(board, 'X') == True:
        print('You won!')
        break;
    elif turn == 10:
        print('Draw')
        break;
    else:
        if turn % 2 == 0:
            board[make_move(board, user_symbol, computer_symbol)] = computer_symbol
            print('Computer move: ')
            turn += 1
        else:
            move = int(input('Enter move(1-9): ')) - 1
            if board[move] == ' ':
                board[move] = user_symbol
                turn += 1
            else:
                print('Please make a move on an empty square')

'''
##############
#   OUTPUT   #
##############
Enter your symbol X or O: X
 | |
 | |
 | |
Enter move(1-9): 5
 | |
 |X|
 | |
Computer move:
 | |O
 |X|
 | |
Enter move(1-9): 1
X| |O
 |X|
 | |
Computer move:
X| |O
 |X|
 | |O
Enter move(1-9): 4
X| |O
X|X|
 | |O
Computer move:
X| |O
X|X|O
 | |O
The computer won!
'''
