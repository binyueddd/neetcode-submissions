class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cur = 0
        n = len(nums)
        min_len = float('inf')
        start = 0

        for i, num in enumerate(nums):
            cur += num

            while cur >= target:
                min_len = min(min_len, i-start+1)
                cur -= nums[start]
                start+=1


        return min_len if min_len != float('inf') else 0    
            