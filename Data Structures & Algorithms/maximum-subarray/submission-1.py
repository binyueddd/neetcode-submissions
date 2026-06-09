class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)

        def dfs(i):
            if i==0:
                return nums[0]
            
            return max(nums[i],dfs(i-1)+nums[i])
        
        ans=float('-inf')

        for i in range(n):
            ans=max(ans,dfs(i))
        return ans