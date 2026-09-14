class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        edges = []

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1,n):
                x2, y2 = points[j]
                dist = abs(x1-x2)+abs(y1-y2)
                edges.append((dist,i,j))
        
        edges.sort()
        
        parent = list(range(n))
        size = [1]*n

        def find(x):
            while x != parent[x]:
                parent[x]=parent[parent[x]]
                x = parent[x]
            
            return x
        
        def union(a,b):
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return False

            if size[root_a]<size[root_b]:
                root_a, root_b = root_b, root_a

            parent[root_b]=root_a
            size[root_a]+=size[root_b]

            return True
        
        cost = 0
        used_edges=0

        for dist, a, b in edges:
            if union(a,b):
                cost+=dist
                used_edges+=1

                if used_edges==n-1:
                    break
        
        return cost