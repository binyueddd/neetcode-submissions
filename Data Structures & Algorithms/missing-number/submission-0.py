class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen=set(nums)
        for num in range(len(nums)+1):
            if num not in seen:
                return num