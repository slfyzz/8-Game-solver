from implementation.Solver import Solver
from implementation.Fringe import Queue, Stack, PriorityQueue
from implementation.priorityCalc import ManhattanDistance, EuclideanDistance
from UI.gui.gui import GUI
from statistcs.statistics import Statics


#Statics().compare()
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


x = Solver(getFringe(strategy), initial_state=inputMatrix, goal=createGoal(len(inputMatrix), len(inputMatrix[0])))
a, b, c = x.solve()

lst = []
while c is not None:
    lst.append(c.getCurrentState())
    c = c.getPrevState()

lst.reverse()
x.ShowInfo()
gui.showTrace(lst)
