class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        if len(nums)==1:
            return nums[0]
        
        def rob_line(subnums):
            dp=[0,0]
            for i in range(len(subnums)):
                dp[0],dp[1]=dp[1],max(dp[1],dp[0]+subnums[i])
            return dp[1]
        
        return max(rob_line(nums[:-1]), rob_line(nums[1:]))
