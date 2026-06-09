from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @cache
        def dfs(i, remain):
            if i < 0:
                return 1 if remain == 0 else 0

            # nums[i] 前面放 "+"
            plus = dfs(i - 1, remain - nums[i])

            # nums[i] 前面放 "-"
            minus = dfs(i - 1, remain + nums[i])

            return plus + minus

        return dfs(n - 1, target)