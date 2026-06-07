class UnionFind:
    def __init__(self,n):
        self.parent=list(range(n+1))
    
    def find(self,x):
        while x!=self.parent[x]:
            x=self.parent[x]
        return x
    
    def union(self,x,y):
        rootA=self.find(x)
        rootB=self.find(y)

        if rootA==rootB:
            return False
        
        self.parent[rootB]=rootA
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        uf=UnionFind(n)
        for a,b in edges:
            if not uf.union(a,b):
                return [a,b]
        




