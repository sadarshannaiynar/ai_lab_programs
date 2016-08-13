class state:
    def __init__(self, x, y):
        self.x = x
        self.y = y

start = state(0, 0)
goal = state(2, 0)
cap_jug1 = 5
cap_jug2 = 4

def fill(cur_state):
    print('(' + str(cur_state.x) + ',' + str(cur_state.y) + ')-->', end='')
    if (cur_state.x == goal.x) and (cur_state.y == goal.y):
        print('GOAL')
        return True
    if cur_state.x == 0:
        fill(state(cap_jug1, cur_state.y))
    elif (cur_state.x > 0) and (cur_state.y < cap_jug2):
        x_to_y = min(cur_state.x, (cap_jug2 - cur_state.y))
        fill(state(cur_state.x - x_to_y, cur_state.y + x_to_y))
    elif (cur_state.x > 0) and (cur_state.y == cap_jug2):
        fill(state(cur_state.x, 0))

fill(start)

'''
##############
#   OUTPUT   #
##############

(0,0)-->(5,0)-->(1,4)-->(1,0)-->(0,1)-->(5,1)-->(2,4)-->(2,0)-->GOAL
'''
