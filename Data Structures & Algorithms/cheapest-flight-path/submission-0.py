class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph=defaultdict(list)

        for u,v,price in flights:
            graph[u].append((v,price))

        ans=float('inf')
        max_edges=k+1

        def dfs(airport, cost, edge_left):
            if airport==dst:
                nonlocal ans
                ans=min(ans,cost)
                return
            
            if edge_left==0:
                return
            
            if cost>=ans:
                return
        
            for nbr, price in graph[airport]:
                dfs(nbr, price+cost, edge_left-1)
        
        dfs(src,0,k+1)
        return ans if ans!=float('inf') else -1

