class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        
        graph=defaultdict(list)
        for pre,nxt in edges:
            graph[pre].append(nxt)
            graph[nxt].append(pre)
        
        visited = set()

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for nbr in graph[node]:
                dfs(nbr)
        
        dfs(0)
        return len(visited)==n
            
