class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        m=len(grid)
        n=len(grid[0])
        res=0

        def dfs(r,c):
            if r<0 or r>=m or c<0 or c>=n:
                return 0
            
            if grid[r][c]==0:
                return 0
            

            area=1
            grid[r][c]=0

            for dx,dy in directions:
                area+=dfs(r+dx,c+dy)

            return area
            
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    res=max(res,dfs(i,j))
        
        return res
            
