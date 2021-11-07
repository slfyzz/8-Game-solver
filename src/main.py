from Solver import Solver
from Fringe import Queue, Stack, PriorityQueue
from priorityCalc import ManhattanDistance, EuclideanDistance
from gui import GUI
from validator import isSolvable


# Factory method from Queues
def getFringe(strategyType):
    if strategyType == 'BFS':
        print("BFS")
        return Queue()
    elif strategyType == 'DFS':
        print("DFS")
        return Stack()
    elif strategyType == 'A* with Manhattan':
        print("Manhattan")
        return PriorityQueue(ManhattanDistance())
    else:
        print("Euclidean")
        return PriorityQueue(EuclideanDistance())


# To create different default goals.
def createGoal(n, m):
    goal = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(i * m + j)
        goal.append(tuple(row))
    return tuple(goal)


# Starting Gui, and getting the input (Strategy string and the matrix)
gui = GUI()
inputMatrix, strategy = gui.getInputMatrix()

# Check if it's solvable.
solvable = isSolvable(inputMatrix)

# If it's not solvable, escape all these computations
if not solvable:
    print("It's not solvable")
else:
    x = Solver(getFringe(strategy), initial_state=inputMatrix, goal=createGoal(len(inputMatrix), len(inputMatrix[0])))
    a, b, c = x.solve()

    lst = []
    while c is not None:
        lst.append(c.getCurrentState())
        c = c.getPrevState()

    lst.reverse()
    x.ShowInfo()
    gui.showTrace(lst)
