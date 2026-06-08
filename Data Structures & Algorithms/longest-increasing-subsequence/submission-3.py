from functools import cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        @cache
        def dfs(i,prev):
            if i==n:
                return 0
            
            skip=dfs(i+1,prev)
            take=0
            if prev==-1 or nums[i]>nums[prev]:
                take=1+dfs(i+1,i)
            
            return max(skip,take)
        
        return dfs(0,-1)