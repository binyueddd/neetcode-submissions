class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        n = len(grid)
    
        heap = [(grid[0][0],0,0)]

        visited =set()

        while heap:
            time, r, c = heapq.heappop(heap)

            if (r,c) in visited:
                continue
            
            visited.add((r,c))

            if r==n-1 and c==n-1:
                return time

            for dx, dy in directions:
                x = r+dx
                y = c+dy

                if x < 0 or x>=n or y<0 or y>=n or (x,y) in visited:
                    continue
                
                new_time = max(time ,grid[x][y])
                heapq.heappush(heap,(new_time,x,y))