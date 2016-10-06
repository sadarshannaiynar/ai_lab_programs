class cell():

    def __init__(self, x, y, g, parent) :
        self.x = x
        self.y = y
        self.g = g
        self.f = 0
        self.parent = parent

def neighbors(node, rows, columns):
    neighbors_list = []
    if ((node.x + 1) < rows) and ((node.y + 1) < columns):
        neighbors_list.append(cell(node.x + 1, node.y + 1, node.g + 1.414, node))
    if ((node.x - 1) > -1) and ((node.y - 1) > -1):
        neighbors_list.append(cell(node.x - 1, node.y - 1, node.g + 1.414, node))
    if ((node.x + 1) < rows) and ((node.y - 1) > -1):
        neighbors_list.append(cell(node.x + 1, node.y - 1, node.g + 1.414, node))
    if ((node.x - 1) > -1) and ((node.y + 1) > columns):
        neighbors_list.append(cell(node.x - 1, node.y + 1, node.g + 1.414, node))
    if (node.x + 1) < rows:
        neighbors_list.append(cell(node.x + 1, node.y, node.g + 1, node))
    if (node.x - 1) > -1:
        neighbors_list.append(cell(node.x - 1, node.y, node.g + 1, node))
    if (node.y + 1) < columns:
        neighbors_list.append(cell(node.x, node.y + 1, node.g + 1, node))
    if (node.y - 1) > -1:
        neighbors_list.append(cell(node.x, node.y - 1, node.g + 1, node))
    return neighbors_list

def heuristic(node, goal):
    dx = abs(node.x - goal.x)
    dy = abs(node.y - goal.y)
    return  ((dx + dy) + (1.414 - 2) * min(dx,dy))

def get_cheapest(nodes):
    cost = [node.f for node in nodes]
    return nodes[cost.index(min(cost))]

def construct_path(node, board):
    board[node.x][node.y] = 1
    path = [node]
    while node.parent != '':
        node = node.parent
        path.insert(0, node)
        board[node.x][node.y] = 1
    for i in path:
        print('(' + str(i.x + 1) + ',' + str(i.y + 1) + ')-->', end='')
    print('GOAL\n')
    return print_board(board)

def astar(start, goal, board, rows, columns):
    open_list = [start]
    closed_list = []
    start.f = start.g + heuristic(start, goal)
    while len(open_list) > 0:
        node = get_cheapest(open_list)
        if (node.x == goal.x) and (node.y == goal.y):
            return construct_path(node, board)
        closed_list.append(open_list.pop(get_index(node, open_list)))
        for neighbor in neighbors(node, rows, columns):
            if get_index(neighbor, closed_list) == -1:
                neighbor.f = neighbor.g + heuristic(neighbor, goal)
                index = get_index(neighbor, open_list)
                if index == -1:
                    open_list.append(neighbor)
                else:
                    if neighbor.g < open_list[index].g:
                        open_list[index].g = neighbor.g
                        open_list[index].parent = neighbor.parent
    print('Not Possible')

def get_index(node, nodes):
    for i in nodes:
        if (i.x == node.x) and (i.y == node.y):
            return nodes.index(i)
    return -1

def print_board(board):
    for i in board:
        for j in i:
            print(str(j) + ' ',end='')
        print('')

board = list()
rows = int(input('Enter rows: '))
columns = int(input('Enter columns: '))
for i in range(rows):
    board.append(list())
    for j in range(columns):
        board[i].append(0)
print('The Board: ')
print_board(board)
start = cell(int(input('\nEnter start x: ')) - 1, int(input('Enter start y: ')) - 1, 0, '')
goal = cell(int(input('Enter goal x: ')) - 1, int(input('Enter goal y: ')) - 1, 0, '')
print('\nSolution: ')
astar(start, goal, board, rows, columns)

'''
##############
#   OUTPUT   #
##############

Enter rows: 4
Enter columns: 6
The Board:
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

Enter start x: 1
Enter start y: 1
Enter goal x: 4
Enter goal y: 6

Solution:
(1,1)-->(2,2)-->(2,3)-->(3,4)-->(4,5)-->(4,6)-->GOAL

1 0 0 0 0 0
0 1 1 0 0 0
0 0 0 1 0 0
0 0 0 0 1 1

'''
