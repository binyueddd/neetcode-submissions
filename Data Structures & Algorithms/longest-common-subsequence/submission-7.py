class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        memo={}
        def dfs(i,j):
            if i==m or j==n:
                return 0
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            if text1[i]==text2[j]:
                ans = dfs(i+1,j+1)+1
            else:
                ans = max(dfs(i,j+1),dfs(i+1,j))
            
            memo[(i,j)]=ans
            
            return ans
        
        return dfs(0,0)