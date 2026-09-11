class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        m=len(heights)
        n=len(heights[0])
        directions=[(1,0),(-1,0),(0,1),(0,-1)]

        pacific=set()
        atlantic=set()

        def dfs(r,c,visited):
           
            visited.add((r,c))

            for dx,dy in directions:
                x,y= r+dx, c+dy
                if x<0 or x>= m or y<0 or y>=n or (x,y) in visited:
                    continue
                
                if heights[x][y]<heights[r][c]:
                    continue
                
                dfs(x,y,visited)
        
        for i in range(m):
            dfs(i,0,pacific)
        for j in range(n):
            dfs(0,j,pacific)
        for i in range(m):
            dfs(i,n-1,atlantic)
        for j in range(n):
            dfs(m-1,j,atlantic)
        
        res=[]

        for r in range(m):
            for c in range(n):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])

        return res