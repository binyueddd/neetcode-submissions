class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water=0
        start=0
        end=len(heights)-1
        while start<end:
            cur=min(heights[start],heights[end])*(end-start)
            max_water=max(max_water,cur)
            if heights[start]>heights[end]:
                end-=1
            else:
                start+=1
        return max_water