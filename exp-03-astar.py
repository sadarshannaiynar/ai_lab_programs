class cell():

    def __init__(self, x, y, g, parent) :
        self.x = x
        self.y = y
        self.g = g
        self.h = 0
        self.f = 0
        self.parent = parent

def neighbors(node):
    neighbors_list = []
    if ((node.x + 1) != 5) and ((node.y + 1) != 5):
        neighbors_list.append(cell(node.x + 1, node.y + 1, node.g + 1.414, node))
    if ((node.x - 1) != -1) and ((node.y - 1) != -1):
        neighbors_list.append(cell(node.x - 1, node.y - 1, node.g + 1.414, node))
    if ((node.x + 1) != 5) and ((node.y - 1) != -1):
        neighbors_list.append(cell(node.x + 1, node.y - 1, node.g + 1.414, node))
    if ((node.x - 1) != -1) and ((node.y + 1) != 5):
        neighbors_list.append(cell(node.x - 1, node.y + 1, node.g + 1.414, node))
    if (node.x + 1) != 5:
        neighbors_list.append(cell(node.x + 1, node.y, node.g + 1, node))
    if (node.x - 1) != -1:
        neighbors_list.append(cell(node.x - 1, node.y, node.g + 1, node))
    if (node.y + 1) != 5:
        neighbors_list.append(cell(node.x, node.y + 1, node.g + 1, node))
    if (node.y - 1) != -1:
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
    while node.parent != '':
        node = node.parent
        board[node.x][node.y] = 1
    return print_board(board)

def astar(start, goal, board):
    open_list = [start]
    closed_list = []
    start.f = start.g + heuristic(start, goal)
    while len(open_list) > 0:
        node = get_cheapest(open_list)
        if (node.x == goal.x) and (node.y == goal.y):
            return construct_path(node, board)
        closed_list.append(open_list.pop(get_index(node, open_list)))
        for neighbor in neighbors(node):
            if get_index(neighbor, closed_list) == -1:
                neighbor.f = neighbor.g + heuristic(neighbor, goal)
                index = get_index(neighbor, open_list)
                if index == -1:
                    open_list.append(neighbor)
                else:
                    if neighbor.g < open_list[index].g:
                        open_list[index].g = neighbor.g
                        open_list[index].parent = neighbor.parent
    return False

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

start = cell(0, 0, 0, '')
goal = cell(4, 4, 0, '')
board = [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]
print('The Board: ')
print_board(board)
print('\nSolution: ')
astar(start, goal, board)
