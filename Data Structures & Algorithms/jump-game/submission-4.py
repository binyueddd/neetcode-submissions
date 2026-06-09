class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest=nums[0]
        for i in range(1,len(nums)):
            if i>farthest:
                return False
            
            farthest=max(farthest,i+nums[i])
            if farthest>=len(nums)-1:
                return True
        
        return True