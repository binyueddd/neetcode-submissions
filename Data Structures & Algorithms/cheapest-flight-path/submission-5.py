class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')]*n
        prices[src]=0

        for _ in range(k+1):
            tmp = prices[:]

            for u,v, cost in flights:
                if prices[u]==float('inf'):
                    continue
                
                if prices[u]+cost < tmp[v]:
                    tmp[v] = prices[u]+cost
            
            prices = tmp
        
        return prices[dst] if prices[dst] != float('inf') else -1