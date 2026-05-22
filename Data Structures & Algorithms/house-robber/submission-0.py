class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        dp=[0,0]

        for i, num in enumerate(nums):
            dp[1],dp[0]=max(dp[1],dp[0]+nums[i]),dp[1]
        
        return dp[1]