class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        occurs = set(nums)
        count=1
        max_count=1
        
        for num in nums:
            if num-1 not in occurs:
                cur = num
                count=1

                while cur+1 in occurs:
                    cur+=1
                    count+=1
            max_count = max(max_count, count)
        return max_count