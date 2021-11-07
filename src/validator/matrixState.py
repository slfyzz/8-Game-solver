from abc import ABC, abstractmethod

class matrixState(ABC) :
    @abstractmethod
    def isValid(self):
        pass

    @abstractmethod
    def message(self):
        pass


class validState(matrixState,ABC):
    def __init__(self):
        super().__init__()

    def isValid(self):
        return True

    
    def message(self):
        return "Valid"
    
    
class unsolvable(matrixState,ABC):
    def __init__(self):
        super().__init__()

    def isValid(self):
        return False

    def message(self):
        return "unsolvable matrix"
    
    
class dublicatesMatrix(matrixState,ABC):
    def __init__(self , v ):
        self.v = v
        super().__init__()
    def isValid(self):
        return False

    def message(self):
        return "value " + str(self.v) + " is dublicatesis " 
    
    
class sparseMatrix(matrixState,ABC):
    def __init__(self ):
        super().__init__()
    def isValid(self):
        return False

    def message(self):
        return " matrix has some empty cell" 
    
    
    
    
    
    
    
    
    