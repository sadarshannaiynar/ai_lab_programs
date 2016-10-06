from copy import deepcopy

# Class Play to hold board and heuristic
class Play:
    def __init__(self, board, g, parent):
         self.board = board
         self.f = 0
         self.g = g
         self.h = 0
         self.parent = parent

# Get board input
def get_board_input():
    board = list()
    for i in range(3):
        board.append([i for i in input().split()])
    return board

# Make the move
def make_move(board, cur_i, cur_j, next_i, next_j):
    board[cur_i][cur_j] = board[next_i][next_j]
    board[next_i][next_j] = 'N'
    return board

# Get the coordinate of the node
def get_coordinate(board, node):
    for i in board:
        if node in i:
            return [i.index(node), board.index(i)]

# Determine the move
def determine_move(node):
    successors = list()
    j = 0
    i = 0
    for row in node.board:
        if 'N' in row:
            j = row.index('N')
            i = node.board.index(row)
    # Up move
    if i != 0:
         successors.append(Play(make_move(deepcopy(node.board), i, j, i - 1, j), node.g + 1, node))
    # Down move
    if i != 2:
        successors.append(Play(make_move(deepcopy(node.board), i, j, i + 1, j), node.g + 1, node))
    # Left move
    if j != 0:
        successors.append(Play(make_move(deepcopy(node.board), i, j, i, j - 1), node.g + 1, node))
    # Right move
    if j != 2:
        successors.append(Play(make_move(deepcopy(node.board), i, j, i, j + 1), node.g + 1, node))
    return successors

# Manhattan Distance heursitic function
def heuristic(start, goal):
    man_heuristic = 0
    for i in start.board:
        for j in i:
            x, y = get_coordinate(goal.board, j)
            dx = abs(i.index(j) - x)
            dy = abs(start.board.index(i) - y)
            man_heuristic += (dx + dy)
    return man_heuristic

# Get cheapest node
def get_cheapest(open_list):
    min_heuristic = 99999
    min_node = Play(None, 0, None)
    for i in open_list:
        if i.f < min_heuristic:
            min_heuristic = i.f
            min_node = i
    return min_node

# Check whether node is a goal node
def check_goal(board, goal):
    for i in range(3):
        if board[i] != goal.board[i]:
            return False
    return True

# Get index of a node
def get_index(node, nodes):
    for i in range(len(nodes)):
        if node.board == nodes[i].board:
            return i
    return -1

# A* algorithm for shortest path
def astar(start, goal):
    open_list = [start]
    closed_list = list()
    start.f = start.g + heuristic(start, goal)
    while len(open_list) > 0:
        node = get_cheapest(open_list)
        if(check_goal(node.board, goal) == True):
            return construct_path(node)
        closed_list.append(open_list.pop(get_index(node, open_list)))
        for successor in determine_move(node):
            if get_index(successor, closed_list) == -1:
                successor.f = successor.g + heuristic(successor, goal)
                index = get_index(successor, open_list)
                if index == -1:
                    open_list.append(successor)
                else:
                    if successor.g < open_list[index].g:
                        open_list[index].g = successor.g
                        open_list[index].parent = successor.parent
    print('No possible solution')

# Display the board
def display_board(board):
    for i in board:
        print(i)

# Construt the path to solution
def construct_path(node):
    path = [node]
    while node.parent != None:
        node = node.parent
        path.insert(0, node)
    j = 1
    for i in path:
        print('Turn %s:' % (j))
        display_board(i.board)
        print()
        j += 1

print('Enter board starting state: ')
start = Play(get_board_input(), 0, None)
print('Enter goal state: ')
goal = Play(get_board_input(), 0, None)
solve = [j for i in start.board for j in i if j != 'N']
count_inv = 0
for i in range(len(solve)):
    for j in range(i + 1, len(solve)):
        if solve[i] > solve[j]:
            count_inv += 1
if count_inv % 2 == 0:
    astar(start, goal)
else:
    print('Not solvable')

'''
##############
#   OUTPUT   #
##############
SOLVABLE OUTPUT:
Enter board starting state:
1 2 3
4 N 5
7 8 6
Enter goal state:
1 2 3
4 5 6
7 8 N
Turn 1:
['1', '2', '3']
['4', 'N', '5']
['7', '8', '6']

Turn 2:
['1', '2', '3']
['4', '5', 'N']
['7', '8', '6']

Turn 3:
['1', '2', '3']
['4', '5', '6']
['7', '8', 'N']

UNSOLVABLE OUTPUT:
Enter board starting state:
7 N 2
8 5 3
6 4 1
Enter goal state:
1 2 3
4 5 6
7 8 N
Not solvable
'''
