class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph=defaultdict(list)

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited=set()
        count=0

        def dfs(node):
            for nbr in graph[node]:
                if nbr in visited:
                    continue
                
                visited.add(nbr)
                dfs(nbr)
        
        res=0
        for node in range(n):
            if node not in visited:
                dfs(node)
                res+=1
        return res