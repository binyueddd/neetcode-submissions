class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        target+=sum(nums)
        if target<0 or target%2:
            return 0
        target//=2
        def dfs(i,remain):
            if i<0:
                return 1 if remain==0 else 0
            
            if nums[i]>remain:
                return dfs(i-1,remain)
            
            return dfs(i-1,remain-nums[i])+dfs(i-1,remain)
        
        return dfs(n-1,target)
            
