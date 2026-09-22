class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<2:
            return nums[0]
        
        dp0, dp1 = nums[0],max(nums[1],nums[0])
        for i in range(2,len(nums)):
            dp0, dp1 = dp1, max(dp0+nums[i],dp1)
        return dp1
        
