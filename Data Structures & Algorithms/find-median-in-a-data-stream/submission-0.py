class MedianFinder:

    def __init__(self):
        self.small=[]
        self.large=[]

    def addNum(self, num: int) -> None:
        if len(self.small)==len(self.large):
            heapq.heappush(self.small,-num)
            large_add=-heapq.heappop(self.small)
            heapq.heappush(self.large,large_add)
        else:
            heapq.heappush(self.large,num)
            small_add=heapq.heappop(self.large)
            heapq.heappush(self.small,-small_add)



    def findMedian(self) -> float:
        if len(self.large)>len(self.small):
            return self.large[0]
        else:
            return (-self.small[0]+self.large[0])/2
        