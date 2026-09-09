class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        m = len(grid)
        n = len(grid[0])

        def dfs(area, r, c):
            if r<0 or r>=m or c<0 or c>=n:
                return area
            
            if grid[r][c]==0:
                return area
            
            grid[r][c]=0
            area+=1

            for x,y in direction:
                area = dfs(area,r+x,c+y)
            
            return area
        
        res=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    res = max(res,dfs(0,i,j))
    
        return res