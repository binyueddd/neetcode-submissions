class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        
        directions=[(0,1),(1,0),(0,-1),(-1,0)]

        queue=deque()
        fresh=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    queue.append((i,j))
                if grid[i][j]==1:
                    fresh+=1
        
        if fresh==0:
            return 0

        minutes=0
        while queue and fresh>0:
            length=len(queue)
            for _ in range(length):
                r,c=queue.popleft()
                for dx,dy in directions:
                    x,y=r+dx,c+dy
                    if x<0 or x>=m or y<0 or y>=n or grid[x][y]!=1:
                        continue

                    grid[x][y]=2
                    fresh-=1
                    queue.append((x,y))
            minutes+=1
        
        return minutes if fresh==0 else -1

    