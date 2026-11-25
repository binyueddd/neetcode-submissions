class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache={}
        m=len(matrix)
        n = len(matrix[0])

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        visited = [False*n for _ in range(m)]

        def dfs(i,j):
            ans=1
            if (i,j) in cache:
                return cache[(i,j)]

            for dx, dy in directions:
                x,y = i+dx, j+dy
                if 0<=x<m and 0<=y<n and matrix[i][j]<matrix[x][y]:
                    ans = max(ans, 1+dfs(x,y))
            
            cache[(i,j)]=ans
            return ans
        
        result = 0
        for i in range(m):
            for j in range(n):
                result = max(result, dfs(i,j))
        
        return result