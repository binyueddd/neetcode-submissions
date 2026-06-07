class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions=[(-1,0),[0,1],[1,0],[0,-1]]
        m=len(grid)
        n=len(grid[0])

        def dfs(r,c):
            if r<0 or r>=m or c<0 or c>=n:
                return
            
            if grid[r][c]=="0":
                return
            
            grid[r][c]="0"

            for i,j in directions:
                dfs(r+i,c+j)
            
        res=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    res+=1
                    dfs(i,j)

        return res