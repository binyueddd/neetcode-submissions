class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        target = total//2
        if total%2 == 1:
            return False
        
        n=len(nums)
        cache={}
        def dfs(i,remain):
            if remain == 0:
                return True
            key=(i,remain)
            if key in cache:
                return cache[key]

            if remain<0:
                return False
            
            if i==n:
                return False
            
            
            skip = dfs(i+1,remain)
            keep = dfs(i+1,remain-nums[i])
            cache[key]=skip or keep
            return cache[key]
        return dfs(0,target)
