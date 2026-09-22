class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        def houserob(houses):
            dp0,dp1 = 0,0
            for money in houses:
                dp0,dp1 = dp1, max(dp0+money,dp1)
            return dp1
        
        return max(houserob(nums[:-1]),houserob(nums[1:]))