class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        is_appear=set()
        
        for num in nums:
            if num in is_appear:
                return True
            is_appear.add(num)
        return False