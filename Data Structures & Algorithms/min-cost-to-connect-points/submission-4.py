class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        min_dist = [float('inf')]*n
        min_dist[0]=0

        visited = [False]*n
        res=0

        for _ in range(n):
            cur = -1
            for i in range(n):
                if not visited[i] and (cur==-1 or min_dist[i]<min_dist[cur]):
                    cur= i
            
            visited[cur]=True
            res+=min_dist[cur]
            x1, y1=points[cur]

            for nxt in range(n):
                if visited[nxt]:
                    continue
                
                x2, y2 = points[nxt]
                dist = abs(x1-x2)+abs(y1-y2)
                min_dist[nxt]=min(min_dist[nxt], dist)
            
        return res