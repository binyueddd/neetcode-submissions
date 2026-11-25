class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m=len(s)
        n=len(t)
        cache={}
        def dfs(i,j):
            if j==n:
                return 1
            if i==m:
                return 0
            
            if (i,j) in cache:
                return cache[(i,j)]
            
            skip = dfs(i+1,j)
            take = 0
            if s[i]==t[j]:
                take = dfs(i+1,j+1)
            
            cache[(i,j)]=skip+take
            
            return skip+take
        
        return dfs(0,0)

