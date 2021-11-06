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

    while c is not None:
        gui.appendBoard(c.getCurrentState())
        c = c.getPrevState()
    
    gui.showTrace()
