#from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        #@cache
        cache={}
        def dfs(i,hold):
            if i>=n:
                return 0
            if (i,hold) in cache:
                return cache[(i,hold)]

            skip = dfs(i+1, hold)
            #hold: whether have a coin
            if hold:
                trade = prices[i]+dfs(i+2, False)
                
            
            else:
                trade = -prices[i]+dfs(i+1,True)


            ans = max(skip, trade)
            cache[(i,hold)]=ans
            return ans
        return dfs(0,False)