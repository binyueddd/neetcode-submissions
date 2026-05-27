class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        res=0
        max_left=0
        max_right=0

        while left<right:
            max_left=max(height[left],max_left)
            max_right=max(height[right],max_right)

            if max_left<=max_right:
                res+=max_left-height[left]
                left+=1
            else:
                res+=max_right-height[right]
                right-=1
        
        return res
            

