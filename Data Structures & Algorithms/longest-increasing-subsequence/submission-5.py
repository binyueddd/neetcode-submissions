class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        cache={}
        def dfs(i,prev):
            if i==n:
                return 0
            key=(i,prev)
            if key in cache:
                return cache[key]

            skip = dfs(i+1,prev)
            take = 0
            if nums[i]>nums[prev] or prev==-1:
                take = 1+dfs(i+1,i)
            
            cache[key] = max(take, skip)
            return cache[key]
        
        return dfs(0,-1)