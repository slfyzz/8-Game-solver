directions = [1, -1, 0, 0]


class State(object):
    def __init__(self, matrix: tuple, priority=0, prev_state=None):
        self.matrix = matrix
        self.priority = priority
        self.prevState = prev_state

    def expand(self):
        i, j = self.findZero()
        ans = []
        limit = len(self.matrix)
        for z in range(0, 4):
            # new place for the zero
            x = directions[z] + i
            y = directions[3 - z] + j
            if 0 <= x < limit and 0 <= y < limit and (self.prevState is None or self.prevState.matrix[x][y] != 0):
                ans.append(self.createState(i, j, x, y))
        return ans

    def findZero(self):
        return [(ix, iy) for ix, row in enumerate(self.matrix) for iy, i in enumerate(row) if i == 0][0]

    def createState(self, oldX, oldY, newX, newY):
        # Making the state immutable.
        matrix = []
        for row in self.matrix:
            matrix.append(list(row))
        self.swap(matrix, oldX, oldY, newX, newY)

        for i in range(0, len(matrix)):
            matrix[i] = tuple(matrix[i])
        matrix = tuple(matrix)
        return State(matrix, self.priority + 1, self)

    def swap(self, matrix: list, oldX, oldY, newX, newY):
        temp = matrix[oldX][oldY]
        matrix[oldX][oldY] = self.matrix[newX][newY]
        matrix[newX][newY] = temp
