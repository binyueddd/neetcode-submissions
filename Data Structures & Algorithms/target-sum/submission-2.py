class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache={}
        def dfs(i, cur):
            if i==len(nums):
                if cur==target:
                    return 1
                else:
                    return 0
            key = (i,cur)
            if key in cache:
                return cache[key]
            
                
            plus = dfs(i+1,cur+nums[i])
            minus = dfs(i+1, cur-nums[i])
            cache[key]=plus+minus

            return plus+minus
        
        return dfs(0,0)
            



