from Solver import Solver
from Fringe import Queue, Stack, PriorityQueue
from priorityCalc import ManhattanDistance, EuclideanDistance
from gui import GUI
from validator import isSolvable
from statistics import Statics


Statics().compare()


# =============================================================================
# gui = GUI()
# inputMatrix = gui.getInputMatrix()
# 
# solvable = isSolvable(inputMatrix)
# if not solvable :
#     print("not solvable ")
# else :
#     x = Solver(Stack(),initial_state=inputMatrix)
#     a, b, c = x.solve()
# 
#     lst = []
#     while c is not None:
#         lst.append(c.getCurrentState())
#         c = c.getPrevState()
# 
#     lst.reverse()
#     gui.showTrace(lst)
# 
# =============================================================================
