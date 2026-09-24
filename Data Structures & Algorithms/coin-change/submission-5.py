
from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dfs(i,remain):
            if remain==0:
                return 0
            
            if i==len(coins):
                return float('inf')
            
            skip = dfs(i+1,remain)

            take = float('inf')
            
            if coins[i]<=remain:
                take = 1+dfs(i,remain-coins[i])
            
            res = min(skip,take)
            return res
        
        return dfs(0,amount) if dfs(0,amount) !=float('inf') else -1
