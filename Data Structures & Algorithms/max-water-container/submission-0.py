class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area=0
        start=0
        end=len(heights)-1
        while start<end:
            cur_area = (end-start)*min(heights[start],heights[end])
            max_area = max(cur_area,max_area)
            if heights[start]<=heights[end]:
                start+=1
            else:
                end-=1
        return max_area