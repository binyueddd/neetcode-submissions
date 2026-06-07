class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        path=[]
        rows=[0]*n
        cols=[0]*n

        def valid(row,col):
            for r in range(row):
                c=cols[r]
                if row+col==r+c or col-row==c-r:
                    return False
            return True

        def dfs(r,c):
            if r==n:
                res.append(["."*col+"Q"+'.'*(n-col-1) for col in cols])
                return
            
            for col in c:
                if valid(r,col):
                    cols[r]=col
                    dfs(r+1,c - {col})
        
        dfs(0,set(range(n)))
        return res
