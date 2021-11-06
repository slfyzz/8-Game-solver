from printer import Printer 
class Info:
    
    __instance = None
    
    
# =============================================================================
#    @staticmethod 
#    def getInstance():
#       if Info.__instance == None:
#          Info()
#       return Info.__instance
#   
#     
#    def __init__(self):
#       if Info.__instance != None:
#          raise Exception("This class is a singleton!")
#       else:
#          Singleton.__instance = self
#          
# =============================================================================
         
         
    def __init__(self, cost , nodesExpanded , searchDepth , runningTime):
        self.cost = cost
        self.nodesExpanded = nodesExpanded
        self.searchDepth = searchDepth
        self.runningTime = runningTime
        
    def printInfo(self) :
        Printer().printKeyAndValue("cost" , self.cost)
        Printer().printKeyAndValue("Nodes Expanded" , self.nodesExpanded)
        Printer().printKeyAndValue("search Depth" , self.searchDepth)
        Printer().printKeyAndValue("running Time" , self.runningTime)
        pass
        
        
        
        
        