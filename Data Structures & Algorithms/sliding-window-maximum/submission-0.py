class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        left=0
        right=k-1
        while right<len(nums):
            cur=nums[left:right+1]
            res.append(max(cur))
            left+=1
            right+=1
        
        return res