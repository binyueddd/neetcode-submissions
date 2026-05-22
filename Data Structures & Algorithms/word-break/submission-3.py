class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #dp[i]=dp[i-len(word)] for word in wordDict or dp[i]
        dp=[False]*(len(s)+1)
        wordset=set(wordDict)
        dp[0]=True
        for i in range(1,len(s)+1):
            for j in range(i):
              if dp[j] and s[j:i] in wordset:
                dp[i]=True
                break
        return dp[-1]