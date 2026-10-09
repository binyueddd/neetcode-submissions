from functools import cache
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        @cache
        def dfs(i):
            if i==0:
                return nums[0],nums[0]
            
            prev_max, prev_min = dfs(i-1)
            x = nums[i]
            cur_max = max(prev_max*x,prev_min*x,x)
            cur_min = min(prev_max*x,prev_min*x,x)
            return cur_max,cur_min
        
        return max(dfs(i)[0] for i in range(len(nums)))