class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph=defaultdict(list)
        tickets.sort(reverse=True)

        for src,dst in tickets:
            graph[src].append(dst)
        
        res=[]

        def dfs(airport):
            while graph[airport]:
                nxt_airport=graph[airport].pop()
                dfs(nxt_airport)

            res.append(airport)

        dfs("JFK")
        return res[::-1]