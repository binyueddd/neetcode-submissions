class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start,new_end=newInterval[0],newInterval[1]
        res=[]
        for i, (start,end) in enumerate(intervals):
            if new_start>end:
                res.append([start,end])
            

            elif new_end<start:
                res.append([new_start,new_end])
                res.extend(intervals[i:])
                return res
            
            else:
                new_start=min(start,new_start)
                new_end=max(end,new_end)
        res.append([new_start,new_end])
        return res