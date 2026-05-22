class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph=defaultdict(list)

        for pre,nxt in edges:
            graph[pre].append(nxt)
            graph[nxt].append(pre)

        visited=set()
        count=0
        
        for node in range(n):
            if node in visited:
                continue
            count += 1
            queue=deque([node])
            visited.add(node)
            while queue:
                cur=queue.popleft()
                
                for nbr in graph[cur]:
                    if nbr not in visited:
                        queue.append(nbr)
                        visited.add(nbr)
            
        return count




