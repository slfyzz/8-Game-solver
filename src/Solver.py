from state import State
from Fringe import Fringe
from config import *
from datetime import datetime
from info import Info
 

class Solver:
    def __init__(self, fringe: Fringe, initial_state=DEFAULT_STATE, goal=DEFAULT_GOAL_STATE):
        self.fringe = fringe
        self.initialState = State(initial_state)
        self.goal = goal
        self.count = 0
        self.start = 0 
        self.end = 0 
        self.cost = 0 
        self.maxDepth = 0 
        

    def solve(self):
        self.start = datetime.now()
        self.fringe.push(self.initialState)
        seen = set()

        while not self.fringe.isEmpty():
            state = self.fringe.pop()
            self.count += 1
            if TRACK_VISITED_NODE and state.getCurrentState() in seen:
                continue

            seen.add(state.getCurrentState())
            if state.equals(DEFAULT_GOAL_STATE):
                self.end = datetime.now()
                self.cost = state.getPriority() 
                return "SUCCESS", self.count, state
            for exp in state.expand():
                self.maxDepth = max(self.maxDepth,exp.getPriority())
                self.fringe.push(exp)
        
        self.end = datetime.now()
        return "FAIL", self.count, None
    
    def getInfo(self):
        return Info(self.cost,self.count,self.maxDepth,str((self.end - self.start).total_seconds()) +" Second")
        
    def ShowInfo(self):
        self.getInfo().printInfo()
        print()
