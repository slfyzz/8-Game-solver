import tkinter as tk

class GUI(object):
    
    def __init__(self):
        self.root = tk.Tk()
        self.boardsCounter = 0

    def appendBoard(self,matrix):
        startRow = self.boardsCounter*4
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                e = tk.Entry(relief=tk.GROOVE)
                e.grid(row=startRow+i, column=j)
                e.insert(tk.END, matrix[i][j])
            
        for i in range(len(matrix)):
            e = tk.Entry(background="black")
            e.grid(row=startRow+3, column=i)
            e.insert(tk.END, ' ')

        self.boardsCounter += 1


    def showTrace(self):
        sb = tk.Scrollbar(orient=tk.VERTICAL)
        sb.grid(row=0, column=1, sticky=tk.NS)
        tk.mainloop()

    def getInputMatrix(self):
        matrix = []
        entries = []
        for i in range(3):
            row = []
            for j in range(3):
                e = tk.Entry(relief=tk.GROOVE)
                row.append(e)
                e.grid(row=i, column=j)
            entries.append(row)

        def assignValues():
            for r in entries:
                row = []
                for e in r :
                    row.append(int(e.get()))
                matrix.append(row)
            self.root.destroy()            

        button = tk.Button(self.root,text="Solve",command=assignValues)
        button.grid(row = 3 , column= 1)
        tk.mainloop()

        for i in range(0, len(matrix)):
            matrix[i] = tuple(matrix[i])
        matrix = tuple(matrix)

        return matrix