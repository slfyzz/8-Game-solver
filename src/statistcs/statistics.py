from datetime import datetime
import random
import implementation.config as config
from validator.validator import isSolvable
from implementation.Fringe import Queue, Stack, PriorityQueue
from implementation.priorityCalc import ManhattanDistance , EuclideanDistance
from implementation.Solver import Solver
from UI.printer import Printer


class Statics :
    
    def __init__(self,n = config.n ,m = config.m ):
        self.n = n 
        self.m =m 
        self.state = [i for i in range (n * m )]
        self.last = [0 for i in range(n * m )]
    def convertToMatrix(self,arr):
        mat = []
        cur = 0 
        for i in range(self.n):
            row = []
            for j in range(self.m):
                row.append(arr[cur])
                cur+=1
            mat.append(tuple(row))
            
        mat =tuple(mat)
        return mat
    
    
    
    def getSeed(self):
        return (datetime.now().microsecond%1000) / 1000
       
    
    
    def generateRandomInitialGrid(self):
        
        random.shuffle(self.state,self.getSeed)
        mat = self.convertToMatrix(self.state)
        while mat==self.last or not isSolvable(mat)  :
            random.shuffle(self.state,self.getSeed)
            mat = self.convertToMatrix(self.state)
        self.last = mat    
        return mat
        
        
    
    def compare(self,tests = 1000):
        for i in range(tests):
             Printer().printHeader("Test : " + str(i + 1))
             initialState = self.generateRandomInitialGrid()
             strategies = [Stack(),Queue(),PriorityQueue(ManhattanDistance()) , PriorityQueue(EuclideanDistance()) ]
             startagirsName = ["DFS" ,"BFS", "A * with  ManhattanDistance" , "A * with EuclideanDistance"]
             Printer().printMatrix(initialState)
             Printer().printEndL()
             cur = 0 
             for startgy in strategies:
                 
                     x = Solver(startgy,initial_state=initialState)
                     a, b, c = x.solve()
                     if a == "FAIL" :
                         Printer.printError("test " + str(i) + " has been faild " )
                         Printer.printMatrix(initialState)
                     else :
                         
                         
                         runningInfo = x.getInfo()
                         Printer().printTitle(startagirsName[cur])
                         Printer().printEndL()
                         runningInfo.printInfo()
                         Printer().printEndL()
                     cur += 1
             Printer().printEndL()
                 
                
                
