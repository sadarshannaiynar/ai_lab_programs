class state:
    def __init__(self, x, y, parent):
        self.x = x
        self.y = y
        self.parent = parent

node_list = []
queue = []

def get_index(node):
    for i in range(len(node_list)):
        if (node.x == node_list[i].x) and (node.y == node_list[i].y):
            return i
    return -1

def add_unique(node):
    if get_index(node) == -1:
        node_list.append(node)
        queue.append(node)

def bfs(start, goal, cap_jug1, cap_jug2):
    global queue
    queue = [start]
    while len(queue) > 0:
        cur_state = queue.pop(0)
        if (cur_state.x == goal.x) and (cur_state.y == goal.y):
            return construct_path(cur_state)
        if cur_state.x == 0:
            add_unique(state(cap_jug1, cur_state.y, cur_state))
        if cur_state.y == 0:
            add_unique(state(cur_state.x, cap_jug2, cur_state))
        if cur_state.x > 0:
            add_unique(state(0, cur_state.y, cur_state))
        if cur_state.y > 0:
            add_unique(state(cur_state.x, 0, cur_state))
        if (cur_state.x > 0) and (cur_state.y < cap_jug2):
            x_to_y = min(cur_state.x, (cap_jug2 - cur_state.y))
            add_unique(state(cur_state.x - x_to_y, cur_state.y + x_to_y, cur_state))
        if (cur_state.x < cap_jug1) and (cur_state.y > 0):
            y_to_x = min(cur_state.y, (cap_jug1 - cur_state.x))
            add_unique(state(cur_state.x + y_to_x, cur_state.y - y_to_x, cur_state))
    print('Not Possible')

def construct_path(state):
    path = [state]
    while state.parent != '':
        state = state.parent
        path.insert(0, state)
    return display_path(path)

def display_path(path):
    for i in path:
        print('(' + str(i.x) + ',' + str(i.y) + ')-->', end='')
    print('GOAL')

start = state(0, 0, '')
goal = state(2, 0, '')
bfs(start, goal, 5, 4)

'''
##############
#   OUTPUT   #
##############

(0,0)-->(5,0)-->(1,4)-->(1,0)-->(0,1)-->(5,1)-->(2,4)-->(2,0)-->GOAL
'''
