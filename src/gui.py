import tkinter as tk
from src.validator import isValidInput


class GUI(object):

    def __init__(self, n=3, m=3):
        self.root = tk.Tk()
        self.boardsCounter = 0
        self.cnt = 0
        self.n = n
        self.m = m
        self.matrix = [["" for i in range(n)] for i in range(m)]
        self.enterdNumber = [0 for i in range(n * m)]

    def appendBoard(self, matrix):
        startRow = self.boardsCounter * 4
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                e = tk.Entry(relief=tk.GROOVE)
                e.grid(row=startRow + i, column=j)
                e.insert(tk.END, matrix[i][j])

        for i in range(len(matrix)):
            e = tk.Entry(background="black")
            e.grid(row=startRow + 3, column=i)
            e.insert(tk.END, ' ')

        self.boardsCounter += 1

    def showTrace(self):
        sb = tk.Scrollbar(orient=tk.VERTICAL)
        sb.grid(row=0, column=1, sticky=tk.NS)
        tk.mainloop()

    def callback(self, sv, i, j):
        s = sv.get()
        l = len(s)
        if l == 0:
            self.enterdNumber[int(self.matrix[i][j])] = 0
            self.matrix[i][j] = ""
            self.cnt -= 1
            return

        if not isValidInput(s, self.n * self.m):
            sv.set(self.matrix[i][j])
            return

        if self.enterdNumber[int(s)] == 1:
            sv.set(self.matrix[i][j])
        else:
            self.enterdNumber[int(s)] = 1
            self.matrix[i][j] = s
            self.cnt += 1

    def buildEntry(self, i, j):

        sv = tk.StringVar()
        sv.trace("w", lambda name, index, mode, sv=sv: self.callback(sv, i, j))

        entry = tk.Entry(self.root, relief=tk.GROOVE, textvariable=sv)
        return entry

    def getInputMatrix(self):
        matrix = []
        entries = []

        for i in range(3):
            row = []
            for j in range(3):
                e = self.buildEntry(i, j)
                row.append(e)
                e.grid(row=i, column=j)
            entries.append(row)

        def assignValues():
            if self.cnt < self.n * self.m:
                return
            for r in entries:
                row = []
                for e in r:
                    row.append(int(e.get()))
                matrix.append(row)
            self.root.destroy()

        button = tk.Button(self.root, text="Solve", command=assignValues)
        button.grid(row=3, column=1)
        tk.mainloop()
        for i in range(0, len(matrix)):
            matrix[i] = tuple(matrix[i])
        matrix = tuple(matrix)

        return matrix
