class State(object):
    def __init__(self, matrix: tuple, priority=0, prev_state=None):
        # Should all these values to be immutable.
        self._matrix = matrix
        self._priority = priority
        self._prevState = prev_state

    def expand(self):
        # expanding is just moving zero around, so we can find the zero and then
        # tries all possible moves, then returns all states.
        directions = [1, -1, 0, 0]
        i, j = self.findZero()
        ans = []
        limit = len(self._matrix)
        for z in range(0, 4):
            # new place for the zero
            x = directions[z] + i
            y = directions[3 - z] + j
            # Check if it's valid.
            if 0 <= x < limit and 0 <= y < limit and \
                    (self._prevState is None or self._prevState.getCurrentState()[x][y] != 0):
                ans.append(self.createState(i, j, x, y))
        return ans

    def findZero(self):
        return [(ix, iy) for ix, row in enumerate(self._matrix) for iy, i in enumerate(row) if i == 0][0]

    def createState(self, oldX, oldY, newX, newY):
        # Making the state immutable.
        matrix = []
        for row in self._matrix:
            matrix.append(list(row))
        self.swap(matrix, oldX, oldY, newX, newY)

        for i in range(0, len(matrix)):
            matrix[i] = tuple(matrix[i])
        matrix = tuple(matrix)
        return State(matrix, self._priority + 1, self)

    def swap(self, matrix: list, oldX, oldY, newX, newY):
        temp = matrix[oldX][oldY]
        matrix[oldX][oldY] = self._matrix[newX][newY]
        matrix[newX][newY] = temp

    def equals(self, matrix: tuple):
        return self._matrix == matrix

    def getCurrentState(self):
        return self._matrix

    def getPriority(self):
        return self._priority

    def getPrevState(self):
        return self._prevState

    def __lt__(self, other):
        if self.__eq__(other):
            return self._priority - other.getPriority()
        return self._matrix < self.getCurrentState()

    def __eq__(self, other):
        return self._matrix == other.getCurrentState()
