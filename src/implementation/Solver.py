from implementation.state import State
from implementation.Fringe import Fringe
from implementation.config import *
from datetime import datetime
from implementation.info import Info


class Solver:
    def __init__(self, fringe: Fringe, initial_state=DEFAULT_STATE, goal=DEFAULT_GOAL_STATE):
        # Get goal, initial state, and the type of fringe from the client.
        self.fringe = fringe
        self.initialState = State(initial_state)
        self.goal = goal

        # To collect statistics about the execution.
        self.count = 0
        self.start = 0
        self.end = 0
        self.cost = 0
        self.maxDepth = 0

    def solve(self):
        # Start timer
        self.start = datetime.now()
        # start the fringe with the first state.
        self.fringe.push(self.initialState)
        # Used to remember if this set is visited before.
        seen = set()

        while not self.fringe.isEmpty():
            state = self.fringe.pop()
            if TRACK_VISITED_NODE and state.getCurrentState() in seen:
                continue
            self.count += 1
            # Remember that state.
            seen.add(state.getCurrentState())
            # If it's the goal, then WOHOO found it
            if state.equals(DEFAULT_GOAL_STATE):
                self.end = datetime.now()
                self.cost = state.getPriority()
                return "SUCCESS", self.count, state
            # Otherwise, expand the node.
            for exp in state.expand():
                self.maxDepth = max(self.maxDepth, exp.getPriority())
                self.fringe.push(exp)

        # Stop the timer
        self.end = datetime.now()
        return "FAIL", self.count, None

    def getInfo(self):
        return Info(self.cost, self.count, self.maxDepth, str((self.end - self.start).total_seconds()) + " Second")

    def ShowInfo(self):
        self.getInfo().printInfoSeperate()
        print()
