

class fenwick :
    
    def __init__(self , len):
        self.len = len +1 
        self.tree = [0 for i in range (self.len)]
        
    def insert(self,index) :
        index+=1
        while index < self.len:
            self.tree[index] += 1
            index += (index & -1 * index )
        pass
    
    def sum(self , index):
        index += 1
        ans = 0 
        while index >0 :
            ans+=self.tree[index]
            index -= (index & -1 * index )
            
        return ans

    def range(self , l ,r ):
        ans = self.sum(r) - self.sum(l-1)
        return ans


def isSolvable(matrix , n = 3, m =3):
    inv = 0 
    l = n * m 
    tree = fenwick(l)
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0 :
                continue
            inv += tree.range(matrix[i][j],l-1)
            tree.insert(matrix[i][j])
    print("num of inversions is " , inv)
    if inv%2 == 0:
        return True
    return False

def isValidInput(s,l):
    if not s.isdigit():
        return False
    c = int(s)
    if c < 0 or c >= l :
        return False
    return True
    