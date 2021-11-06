class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Printer :
    
    
    def printError(self,msg):
        print(bcolors.WARNING + msg + bcolors.ENDC)
        pass


    def printKeyAndValue(self,key,value):
        print(bcolors.OKGREEN+key," :", end =" "),
        print( bcolors.OKBLUE + str(value) ,end =" ")
        pass
    
    def printMatrix(self , mat) :
        for i in mat :
            print(i)
        pass
    
    def printHeader(self,msg):
        print(bcolors.OKCYAN+ msg)
        pass
    def printEndL(self) :
        print()
        pass
    
    def printTitle(self,msg):
        print(bcolors.WARNING + msg,end=" ")
    
    
