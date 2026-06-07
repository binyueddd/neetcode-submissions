class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph=defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited=set()
        
        def dfs(node,parent):
            if node in visited:
                return False
            
            visited.add(node)

            for nbr in graph[node]:
                if nbr==parent:
                    continue
                
                if nbr in visited:
                    return False

                if not dfs(nbr,node):
                    return False

            return True
    
        if not dfs(0,-1):
            return False
        
        return len(visited)==n
            
