import tkinter as tk
from validator import *
import config as conf
import time as time
class GUI(object):

    def __init__(self,n = conf.n ,m  = conf.m):
        self.root = tk.Tk()
        self.boards = []
        self.currentBoard = []
        self.index = 0
        self.n = n
        self.m = m
        self.lastmatrix = [[ "" for i in range(m)] for j in range(n)]
        self.initBoard()

    def initBoard (self):
        for i in range(self.n):
            row = []
            for j in range(self.m):
                e = tk.Entry(relief=tk.GROOVE)
                e.grid(row= i, column=j)
                row.append(e)
            self.currentBoard.append(row)


                    
    def update(self,matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if(matrix[i][j] != 0) :
                    e = tk.Entry(relief=tk.GROOVE)
                else:
                    e = tk.Entry(relief=tk.GROOVE,background='black')
                e.grid(row=i, column=j)
                e.insert(tk.END, matrix[i][j])
                self.currentBoard[i][j] = e

    def showTrace(self,boards):
        self.root = tk.Tk()
        self.boards = boards
        self.update(boards[self.index])

        def next():
            self.index += 1
            self.index = min(self.index,len(boards)-1)
            self.update(boards[self.index])

        def prev():
            self.index -= 1
            self.index = max(self.index,0)
            self.update(boards[self.index])

        def goal():
            self.index = len(boards) - 1
            self.update(boards[self.index])
                
        nextButton = tk.Button(self.root, text="next", command=next)
        prevButton = tk.Button(self.root, text="prev", command=prev)
        goalButton = tk.Button(self.root, text="Goal", command=goal)
        nextButton.grid(row=self.n, column=self.m-1)
        prevButton.grid(row=self.n, column=0)
        goalButton.grid(row=self.n, column=int(self.m/2))
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
                self.ShowScreen(matrixState.message())
                return 
    
            for r in entries:
                row = []
                for e in r:
                    row.append(int(e.get()))
                matrix.append(row)
            self.root.destroy()

        button = tk.Button(self.root, text="Solve", command=assignValues)
        button.grid(row=self.n, column=int(self.m/2))
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
        
    def ShowScreen(self,msg):
        top= tk.Toplevel(self.root)
        top.geometry("750x250")
        top.title("Child Window")
        tk.Label(top, text= msg, font=('Mistral 18 bold')).place(x=150,y=80)
