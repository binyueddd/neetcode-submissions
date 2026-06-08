from functools import cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        directions=[(1,0),(0,1)]
        memo={}
        def dfs(r,c):
            if r==m-1 and c==n-1:
                return 1
            
            if r>=m or c>=n:
                return 0
            if (r,c) in memo:
                return memo[(r,c)]
            memo[(r,c)]=dfs(r,c+1)+dfs(r+1,c)
            return memo[(r,c)]
        return dfs(0,0)