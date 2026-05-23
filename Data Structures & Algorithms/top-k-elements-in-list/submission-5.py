class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket=[[]for _ in range(len(nums)+1)]

        count=Counter(nums)
        for num,freq in count.items():
            bucket[freq].append(num)
        
        res=[]

        for freq in range(len(nums),-1,-1):
            for num in bucket[freq]:
                res.append(num)
                if len(res)==k:
                    return res