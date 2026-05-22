class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start,new_end= newInterval[0],newInterval[1]
        res=[]
        for i,(start,end) in enumerate(intervals):
            if new_end<start:
                res.append((new_start,new_end))
                res.extend(intervals[i:])
                return res
            elif new_start<=end and new_end>=start:
                new_start=min(new_start,start)
                new_end=max(new_end,end)
            else:
                res.append((start,end))
            
            
        res.append((new_start,new_end))
        return res


