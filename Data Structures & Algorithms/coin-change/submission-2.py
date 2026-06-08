from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dfs(remain):
            if remain==0:
                return 0
            if remain<0:
                return float('inf')
            
            best=float('inf')
            
            for coin in coins:
                best=min(best,dfs(remain-coin)+1)
            
            return best
        
        ans=dfs(amount)
        return ans if ans!=float('inf') else -1