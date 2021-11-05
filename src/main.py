from src.Solver import Solver
from src.Fringe import Queue, Stack, PriorityQueue
from src.priorityCalc import ManhattanDistance, EuclideanDistance

x = Solver(Queue())
a, b, c = x.solve()
print(a, b, c.matrix)
ls = []

while c.prevState is not None:
    ls.append(c.matrix)
    c = c.prevState
ls.append(c.matrix)

print('Sequence: ********************\n')
for i in range(len(ls) - 1, -1, -1):
    print(ls[i])
