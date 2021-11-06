from Solver import Solver
from Fringe import Queue, Stack, PriorityQueue
from priorityCalc import ManhattanDistance, EuclideanDistance
from gui import GUI

gui = GUI()
inputMatrix = gui.getInputMatrix()

x = Solver(Queue(),initial_state=inputMatrix)
a, b, c = x.solve()
print(a, b, c.matrix)

while c.prevState is not None:
    gui.appendBoard(c.matrix)
    c = c.prevState
gui.appendBoard(c.matrix)

gui.showTrace()
