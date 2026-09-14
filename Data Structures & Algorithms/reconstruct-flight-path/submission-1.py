class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph=defaultdict(list)

        for src, dst in tickets:
            heapq.heappush(graph[src], dst)

        
        res = []

        def dfs(airport):
            while graph[airport]:
                next_airport = heapq.heappop(graph[airport])
                dfs(next_airport)
            
            res.append(airport)
        
        dfs('JFK')
        return res[::-1]