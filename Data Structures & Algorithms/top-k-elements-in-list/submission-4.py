class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        count=Counter(nums)
        if not nums:
            return []
        res=[]
        for num,freq in count.items():
            heapq.heappush(heap,(freq,num))
            if len(heap)>k:
                heapq.heappop(heap)

        for freq,num in heap:
            res.append(num)
        
        return res