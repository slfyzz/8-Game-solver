from UI.printer import Printer 
class Info:
      
             
         
    def __init__(self, cost , nodesExpanded , searchDepth , runningTime):
        self.cost = cost
        self.nodesExpanded = nodesExpanded
        self.searchDepth = searchDepth
        self.runningTime = runningTime
        
    def printInfo(self , end =" ") :
        Printer().printKeyAndValue("cost" , self.cost , end )
        Printer().printKeyAndValue("Nodes Expanded" , self.nodesExpanded,end)
        Printer().printKeyAndValue("search Depth" , self.searchDepth,end)
        Printer().printKeyAndValue("running Time" , self.runningTime,end)
        pass
    
    def printInfoSeperate(self) :
        self.printInfo("\n")
        
        
        
        
