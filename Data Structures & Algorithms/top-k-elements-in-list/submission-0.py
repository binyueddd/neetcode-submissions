class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count= Counter(nums)
        heap = []
        result=[]
        for num, freq in count.items():
            heapq.heappush(heap, (freq,num))
            if len(heap)>k:
                heapq.heappop(heap)
            
        for _, num in heap:
            result.append(num)
        return result