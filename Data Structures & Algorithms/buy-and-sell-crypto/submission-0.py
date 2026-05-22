class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i][0]: the largest profit whether buy stock in ith day
        dp = [0,-prices[0]]
        profit=0
        for i in range(1, len(prices)):
            dp[0],dp[1]=max(dp[1]+prices[i],dp[0]),max(dp[1],-prices[i])
        return dp[0]

