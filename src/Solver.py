from src.state import State
from src.Fringe import Fringe
from src.config import *


class Solver:
    def __init__(self, fringe: Fringe, initial_state=DEFAULT_STATE, goal=DEFAULT_GOAL_STATE):
        self.fringe = fringe
        self.initialState = State(initial_state)
        self.goal = goal
        self.count = 0

    def solve(self):
        self.fringe.push(self.initialState)
        seen = set()

        while not self.fringe.isEmpty():
            state = self.fringe.pop()
            self.count += 1
            if TRACK_VISITED_NODE and state.matrix in seen:
                continue

            seen.add(state.matrix)
            if state.matrix == DEFAULT_GOAL_STATE:
                return "Success", self.count, state
            for exp in state.expand():
                self.fringe.push(exp)

        return "FAIL", self.count, None
