class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col=len(heights),len(heights[0])
        directions=[(0,1),(0,-1),(1,0),(-1,0)]

        path=0

        pacific=set()
        atlantic=set()

        def dfs(r,c,visited):
            visited.add((r,c))

            for dx,dy in directions:
                x,y=r+dx,c+dy
                if x<0 or x>=row or y<0 or y>=col:
                    continue
                
                if (x,y) in visited:
                    continue
                
                if heights[r][c]>heights[x][y]:
                    continue
                
                dfs(x,y,visited)

        for c in range(col):
            dfs(0, c, pacific)

        for r in range(row):
            dfs(r, 0, pacific)

        # Atlantic: bottom row and right column
        for c in range(col):
            dfs(row - 1, c, atlantic)

        for r in range(row):
            dfs(r, col - 1, atlantic)

        res = []

        for r in range(row):
            for c in range(col):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res
            
