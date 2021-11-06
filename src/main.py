from Solver import Solver
from Fringe import Queue, Stack, PriorityQueue
from priorityCalc import ManhattanDistance, EuclideanDistance
from gui import GUI
from validator import isSolvable
gui = GUI()
inputMatrix = gui.getInputMatrix()
    
solvable = isSolvable(inputMatrix)
if not solvable :
    print("not solvable ")
else :
    x = Solver(Stack(),initial_state=inputMatrix)
    a, b, c = x.solve()
    print(a, b, c.matrix)
    
    while c.prevState is not None:
        gui.appendBoard(c.matrix)
        c = c.prevState
    gui.appendBoard(c.matrix)
    
    gui.showTrace()
