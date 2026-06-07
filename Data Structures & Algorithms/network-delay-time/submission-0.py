class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=defaultdict(list)

        for u,v,t in times:
            graph[u].append((v,t))
        
        dist={i: float('inf') for i in range(1,(n+1))}
        dist[k]=0
    
        heap=[(0,k)]

        while heap:
            cur_time, node=heapq.heappop(heap)

            if cur_time>dist[node]:
                continue
            
            for nbr, weight in graph[node]:
                new_time=cur_time+weight

                if new_time<dist[nbr]:
                    dist[nbr]=new_time
                    heapq.heappush(heap,(new_time,nbr))

        ans=max(dist.values())
        return ans if ans !=float('inf') else -1
