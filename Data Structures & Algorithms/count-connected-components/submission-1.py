class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph=defaultdict(list)

        for pre,nxt in edges:
            graph[pre].append(nxt)
            graph[nxt].append(pre)

        visited=set()
        count=0
        
        def dfs(node):
            for nbr in graph[node]:
                if nbr not in visited:
                    visited.add(nbr)
                    dfs(nbr)

        res=0
        for node in range(n):
            if node not in visited:
                dfs(node)
                res+=1
        return res



