class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row,col=len(grid),len(grid[0])
        
        def dfs(r,c):
            if r<0 or r>=row or c<0 or c>=col:
                return
            
            if grid[r][c]=="0":
                return
            
            grid[r][c]="0"

            for i,j in [(1,0),(0,1),(-1,0),(0,-1)]:
                dfs(r+i,c+j)

        res=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]=="1":
                    res+=1
                    dfs(i,j)
        return res
