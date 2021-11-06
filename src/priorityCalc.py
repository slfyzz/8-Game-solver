from abc import ABC, abstractmethod
from state import State
from math import *


class PriorityCalculation(ABC):

    @abstractmethod
    def calc(self, state: State):
        pass


class ManhattanDistance(PriorityCalculation, ABC):

    def calc(self, state: State):
        cost = 0
        # Assuming the goal is fixed (ordered matrix)
        for i in range(0, len(state.matrix)):
            for j in range(0, len(state.matrix)):
                goalX = state.matrix[i][j] / 3
                goalY = state.matrix[i][j] % 3
                cost += abs(goalX - i) + abs(goalY - j)

        return cost


class EuclideanDistance(PriorityCalculation, ABC):

    def calc(self, state: State):
        cost = 0.0
        # Assuming the goal is fixed (ordered matrix)
        for i in range(0, len(state.matrix)):
            for j in range(0, len(state.matrix)):
                goalX = state.matrix[i][j] / 3
                goalY = state.matrix[i][j] % 3
                cost += sqrt((goalX - i) ** 2 + (goalY - j) ** 2)

        return cost
