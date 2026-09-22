class Solution:
    def trap(self, height: List[int]) -> int:
        res=0
        stack=[]

        for i, h in enumerate(height):
            while stack and h >= height[stack[-1]]:
                bottom_h = height[stack.pop()]
                if not stack:
                    break
                left = stack[-1]
                dh = min(height[left],h)-bottom_h
                res+=dh*(i-left-1)
            stack.append(i)
        return res