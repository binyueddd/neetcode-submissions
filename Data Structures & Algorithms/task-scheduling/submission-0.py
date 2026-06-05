class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        heap=[-freq for freq in count.values()]
        heapq.heapify(heap)

        time=0
        
        while heap:
            cycle=n+1
            tmp=[]
            
            while cycle>0 and heap:
                freq=-heapq.heappop(heap)
                freq-=1
                if freq>0:
                    tmp.append(freq)
                time+=1
                cycle-=1

            for freq in tmp:
                heapq.heappush(heap,-freq)
            
            if heap:
                time+=cycle
        
        return time