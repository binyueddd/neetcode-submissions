class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col=len(heights),len(heights[0])
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        pacific, atlantic=set(),set()

        def dfs(r,c,visit,prevHeight):
            if r<0 or r>=row or c<0 or c>=col:
                return
            
            if (r,c) in visit:
                return
            
            if heights[r][c]<prevHeight:
                return
            
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
        
        for c in range(col):
            dfs(0,c,pacific,heights[0][c])
            dfs(row-1,c,atlantic,heights[row-1][c])
        
        for r in range(row):
            dfs(r,0,pacific,heights[r][0])
            dfs(r,col-1,atlantic,heights[r][col-1])
        

        res = []
        for r in range(row):
            for c in range(col):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append((r,c))

        return res