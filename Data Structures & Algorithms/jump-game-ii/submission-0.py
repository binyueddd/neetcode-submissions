from functools import cache
class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        @cache
        def dfs(i):
            if i>=n-1:
                return 0
            
            best=float('inf')
            for j in range(1,nums[i]+1):
                best=min(best,1+dfs(i+j))
            
            return best
        
        return dfs(0)