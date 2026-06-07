class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m=len(heights)
        n=len(heights[0])
        directions=[(0,1),(1,0),(0,-1),(-1,0)]

        pacific,atlantic=set(),set()

        def dfs(r,c,visited,prevheight):
            if r<0 or r>=m or c<0 or c>=n or (r,c) in visited:
                return
            
            if heights[r][c]<prevheight:
                return

            visited.add((r,c))

            for dx, dy in directions:
                dfs(r+dx,c+dy, visited, heights[r][c])
        
        #Pacific
        for r in range(m):
            dfs(r,0,pacific,heights[r][0])
        
        for c in range(n):
            dfs(0,c,pacific,heights[0][c])

        for r in range(m):
            dfs(r,n-1,atlantic,heights[r][n-1])
        
        for c in range(n):
            dfs(m-1,c, atlantic,heights[m-1][c])

        res=[]
        for i in range(m):
            for j in range(n):
                if (i,j) in pacific and (i,j) in atlantic:
                    res.append([i,j])
        return res