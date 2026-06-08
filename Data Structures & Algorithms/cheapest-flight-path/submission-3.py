class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices=[float('inf')]*n
        # 在当前允许的航班段数内，从 src 到机场 i 的最低价格。
        prices[src]=0

        for _ in range(k+1):
            temp=prices[:]

            for u,v,cost in flights:
                if prices[u]==float('inf'):
                    continue
                
                if prices[u] + cost < temp[v]:
                    temp[v] = prices[u] + cost

            prices = temp

        return prices[dst] if prices[dst] != float("inf") else -1