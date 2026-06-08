from functools import cache

class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        @cache
        def dfs(i):
            if i==n:
                return 1
            
            if s[i]=="0":
                return 0
            
            ways = dfs(i+1)

            if i+1<n and 10<=int(s[i:i+2])<=26:
                ways+=dfs(i+2)
            
            return ways
        
        return dfs(0)