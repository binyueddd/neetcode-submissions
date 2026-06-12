"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        heap=[]
        intervals.sort(key=lambda x: x.start)
        ans=0
        for interval in intervals:
            start,end=interval.start,interval.end
            while heap and heap[0]<=start:
                heapq.heappop(heap)
            
            heapq.heappush(heap,end)
            ans=max(ans,len(heap))
        
        return ans
        