class state:
    def __init__(self, x, y, parent):
        self.x = x
        self.y = y
        self.parent = parent

node_list = []
queue = []
rule_dict = {}

def get_index(node):
    for i in range(len(node_list)):
        if (node.x == node_list[i].x) and (node.y == node_list[i].y):
            return i
    return -1

def add_unique(node, rule_number):
    global rule_dict
    if get_index(node) == -1:
        node_list.append(node)
        queue.append(node)
        rule_dict['(' + str(node.x) + ',' + str(node.y) + ')'] = str(rule_number)

def bfs(start, goal, cap_jug1, cap_jug2):
    global queue
    queue = [start]
    while len(queue) > 0:
        cur_state = queue.pop(0)
        if (cur_state.x == goal.x) and (cur_state.y == goal.y):
            return construct_path(cur_state)
        if cur_state.x == 0:
            add_unique(state(cap_jug1, cur_state.y, cur_state), 1)
        if cur_state.y == 0:
            add_unique(state(cur_state.x, cap_jug2, cur_state), 2)
        if cur_state.x > 0:
            add_unique(state(0, cur_state.y, cur_state), 3)
        if cur_state.y > 0:
            add_unique(state(cur_state.x, 0, cur_state), 4)
        if (cur_state.x > 0) and (cur_state.y < cap_jug2):
            x_to_y = min(cur_state.x, (cap_jug2 - cur_state.y))
            add_unique(state(cur_state.x - x_to_y, cur_state.y + x_to_y, cur_state), 5)
        if (cur_state.x < cap_jug1) and (cur_state.y > 0):
            y_to_x = min(cur_state.y, (cap_jug1 - cur_state.x))
            add_unique(state(cur_state.x + y_to_x, cur_state.y - y_to_x, cur_state), 6)
    print('Not Possible')

def construct_path(state):
    path = [state]
    while state.parent != '':
        state = state.parent
        path.insert(0, state)
    return display_path(path)

def display_path(path):
    global rule_dict
    for i in path:
        print('(' + str(i.x) + ',' + str(i.y) + ')-->', end='')
    print('GOAL')
    rule_dict['(0,0)'] = '0'
    print('State \t Rule')
    for i in path:
        rule = '(' + str(i.x) + ',' + str(i.y) + ')'
        print(rule + ' \t ' + get_rule(rule_dict[rule], i))


def get_rule(rule_number, node):
    if rule_number == '0':
        return 'Start'
    elif rule_number == '1':
        return 'Fill jug 1 with ' + str(node.x) + ' litres'
    elif rule_number == '2':
        return 'Fill jug 2 with ' + str(node.y) + ' litres'
    elif rule_number == '3':
        return 'Empty jug 1'
    elif rule_number == '4':
        return 'Empty jug 2'
    elif rule_number == '5':
        return 'Transfer ' + str(node.parent.x - node.x) + ' litres from jug 1 to jug 2'
    elif rule_number == '6':
        return 'Transfer ' + str(node.parent.y - node.y) + ' litres from jug 2 to jug 1'


cap_jug1 = int(input('Enter jug 1 capacity: '))
cap_jug2 = int(input('Enter jug 2 capacity: '))
x = int(input('Enter goal capacity: '))
start = state(0, 0, '')
goal = state(x, 0, '')
bfs(start, goal, cap_jug1, cap_jug2)

'''
##############
#   OUTPUT   #
##############

Enter jug 1 capacity: 4
Enter jug 2 capacity: 5
Enter goal capacity: 3
(0,0)-->(4,0)-->(0,4)-->(4,4)-->(3,5)-->(3,0)-->GOAL
State    Rule
(0,0)    Start
(4,0)    Fill jug 1 with 4 litres
(0,4)    Transfer 4 litres from jug 1 to jug 2
(4,4)    Fill jug 1 with 4 litres
(3,5)    Transfer 1 litres from jug 1 to jug 2
(3,0)    Empty jug 2

'''
