class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        res=0
        heights.append(0)

        for i, height in enumerate(heights):
            while stack and height<heights[stack[-1]]:
                h=heights[stack.pop()]

                if stack:
                    left_index = stack[-1]
                    right_index = i
                    width = right_index - left_index - 1
                else:
                    width=i
                res=max(res,h*width)
            stack.append(i)
        
        return res