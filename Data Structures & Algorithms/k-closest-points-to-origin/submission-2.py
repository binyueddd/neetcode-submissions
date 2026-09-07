class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for point in points:
            dist = (point[0])**2+(point[1])**2
            heapq.heappush(heap,(-dist, point[0],point[1]))

            if len(heap)>k:
                heapq.heappop(heap)
            
        
        return [[x,y] for _,x,y in heap]