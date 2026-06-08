class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo={}
        def dfs(i,j):
            
            if i==len(text1) or j==len(text2):
                return 0

            if (i,j) in memo:
                return memo[(i,j)]
            
            if text1[i]==text2[j]:
                ans= dfs(i+1,j+1)+1
            else:
                ans=max(dfs(i+1,j),dfs(i,j+1))
            memo[(i,j)]=ans
            return memo[(i,j)]
        
        return dfs(0,0)