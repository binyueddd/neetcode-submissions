class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #dp[i][j]:以text1[:i],text2[:j]最长subsequence
        #dp[i][j]: if text1[i]==text2[j]:dp[i-1][j-1]+1, if text1[i]!=text2[j]:max(dp[i-1][j],dp[i][j-1])
        #单数组 subsequence 问题
        # 比如 LIS：
        # dp[i] = 以 nums[i] 结尾的答案
        # 因为只需要控制一个位置。
        # 双字符串 subsequence 问题
        # 比如 LCS：
        # dp[i][j] = text1 前 i 个字符 和 text2 前 j 个字符 的答案

        # 因为要同时控制两个字符串处理到哪里。

        #包含空字符状态，所以是+1
        dp=[[0]*(len(text2)+1) for _ in range(len(text1)+1)] #注意维度
        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        
        return dp[-1][-1]

