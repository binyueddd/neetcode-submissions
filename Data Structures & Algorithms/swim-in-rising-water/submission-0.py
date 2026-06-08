class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        n=len(grid)

        heap=[(grid[0][0],0,0)]
        visited=set()

        while heap:
            time,r,c=heapq.heappop(heap)

            if (r,c) in visited:
                continue

            visited.add((r,c))

            if r==n-1 and c==n-1:
                return time
            
            for dx,dy in directions:
                x,y=r+dx,c+dy
                if 0<=x<n and 0<=y<n and (x,y) not in visited:
                    new_time=max(time,grid[x][y])
                    heapq.heappush(heap,(new_time,x,y))
                    

