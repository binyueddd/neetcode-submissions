from functools import cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m=len(word1)
        n=len(word2)
        @cache
        def dfs(i,j):
            if i<0:
                return j+1
            if j<0:
                return i+1
            
            if word1[i]==word2[j]:
                return dfs(i-1,j-1)
            
            insert=dfs(i,j-1)
            delete=dfs(i-1,j)
            replace=dfs(i-1,j-1)

            return 1+min(insert,delete,replace)
        
        return dfs(m-1,n-1)
            
