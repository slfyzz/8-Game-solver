from Solver import Solver
from Fringe import Queue, Stack, PriorityQueue
from priorityCalc import ManhattanDistance, EuclideanDistance
from gui import GUI
from validator import isSolvable
from statistics import Statics


# Statics().compare()
 
gui = GUI()
inputMatrix, strategy = gui.getInputMatrix()

solvable = isSolvable(inputMatrix)

if(strategy == 'BFS'):
    x = Solver(Queue(),initial_state=inputMatrix)
    print("BFS")
elif(strategy == 'DFS'):
    x = Solver(Stack(),initial_state=inputMatrix)
    print("DFS")
elif(strategy == 'A* with Manhattan'):
    x = Solver(PriorityQueue(ManhattanDistance),initial_state=inputMatrix)
    print("Manhattan")
elif(strategy == 'A* with Euclidean'):
    x = Solver(PriorityQueue(EuclideanDistance),initial_state=inputMatrix)
    print("Euclidean")

a, b, c = x.solve()
 
lst = []
while c is not None:
    lst.append(c.getCurrentState())
    c = c.getPrevState()
 
lst.reverse()
x.ShowInfo()
gui.showTrace(lst)
