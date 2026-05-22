class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #farest=max(farest,i+nums[i])
        farest=0
        for i in range(len(nums)):
            if i>farest:
                return False
            farest=max(farest, i+nums[i])
        
        return True