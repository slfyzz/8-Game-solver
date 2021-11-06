import tkinter as tk
from validator import *


class GUI(object):

    def __init__(self,n = 3 ,m  = 3):
        self.root = tk.Tk()
        self.boardsCounter = 0
        self.n = n
        self.m = m
        self.lastmatrix = [[ "" for i in range(m)] for j in range(n)]

    def appendBoard(self, matrix):
        startRow = self.boardsCounter * self.n + 1
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                e = tk.Entry(relief=tk.GROOVE)
                e.grid(row=startRow + i, column=j)
                e.insert(tk.END, matrix[i][j])

        for i in range(len(matrix)):
            e = tk.Entry(background="black")
            e.grid(row=startRow + self.n, column=i)
            e.insert(tk.END, ' ')

        self.boardsCounter += 1

    def showTrace(self):
        sb = tk.Scrollbar(orient=tk.VERTICAL)
        sb.grid(row=0, column=1, sticky=tk.NS)
        tk.mainloop()

    def getInputMatrix(self):
        matrix = []
        entries = []

        for i in range(self.n):
            row = []
            for j in range(self.m):
                e = self.buildEntry(i, j)
                row.append(e)
                e.grid(row=i, column=j)
            entries.append(row)

        def assignValues():
            
            matrixState = getMatrixState(self.lastmatrix)
            if not matrixState.isValid():
                self.ShowScreenn(matrixState.message())
                return 
    
            for r in entries:
                row = []
                for e in r:
                    row.append(int(e.get()))
                matrix.append(row)
            self.root.destroy()

        button = tk.Button(self.root, text="Solve", command=assignValues)
        button.grid(row=self.n, column=1)
        tk.mainloop()
        for i in range(0, len(matrix)):
            matrix[i] = tuple(matrix[i])
        matrix = tuple(matrix)

        return matrix



    def callback(self, sv, i, j):
        s = sv.get()
        l = len(s)
        if l == 0:
            self.lastmatrix[i][j] = ""
            return

        if not isValidInput(s, self.n * self.m):
            sv.set(self.lastmatrix[i][j])
            return
        self.lastmatrix[i][j] = s
        pass


    def buildEntry(self, i, j):

        sv = tk.StringVar()
        sv.trace("w", lambda name, index, mode, sv=sv: self.callback(sv, i, j))

        entry = tk.Entry(self.root, relief=tk.GROOVE, textvariable=sv)
        return entry
    def ShowScreenn(self,msg):
        top= tk.Toplevel(self.root)
        top.geometry("750x250")
        top.title("Child Window")
        tk.Label(top, text= msg, font=('Mistral 18 bold')).place(x=150,y=80)
