from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        @cache
        def dfs(i,hold):
            if i>=n:
                return 0
            
            skip = dfs(i+1, hold)
            #hold: whether have a coin
            if hold:
                trade = prices[i]+dfs(i+2, False)
                
            
            else:
                trade = -prices[i]+dfs(i+1,True)


            ans = max(skip, trade)
            return ans
        return dfs(0,False)