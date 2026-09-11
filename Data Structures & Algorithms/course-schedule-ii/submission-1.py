class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        indegree=[0]*numCourses

        for cur, pre in prerequisites:
            graph[pre].append(cur)
            indegree[cur]+=1

        queue=deque()
        for course in range(numCourses):
            if indegree[course]==0:
                queue.append(course)
        
        res=[]
        while queue:
            cur=queue.popleft()
            res.append(cur)
            for nxt in graph[cur]:
                indegree[nxt]-=1
                if indegree[nxt]==0:
                    queue.append(nxt)
        
        return res if len(res)==numCourses else []