class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #dp[i]:到i的最大increasing数组长度
        #dp[i]=dp[i-1]+1 if nums[i]>increasing数组的最大值 else dp[i-1]
        #不对
        #dp[i]:以nums[i]结尾的最长递增子序列长度
        #dp[i]=max(dp[i],dp[j]+1)
        dp=[1]*(len(nums))
        dp[0]=1
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i]=max(dp[i],dp[j]+1)
        
        return max(dp)