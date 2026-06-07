class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m=len(grid)
        n=len(grid[0])
        INF=2147483647

        queue=deque()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    queue.append((i,j))
        
        directions=[(0,1),(0,-1),(1,0),(-1,0)]

        while queue:
            r,c,=queue.popleft()
            
            for dx,dy in directions:
                x,y=r+dx,c+dy
                if x<0 or x>=m or y<0 or y>=n or grid[x][y]!=INF:
                    continue

                
                grid[x][y]=grid[r][c]+1
                queue.append((x,y))
        
        

