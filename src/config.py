

n = 3
m = 3

DEFAULT_GOAL_STATE = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(i*m+j)
    DEFAULT_GOAL_STATE.append(tuple(row))
DEFAULT_GOAL_STATE = tuple(DEFAULT_GOAL_STATE)

DEFAULT_STATE = ((1, 2, 5), (3, 4, 0), (6, 7, 8))
TRACK_VISITED_NODE = True

