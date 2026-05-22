class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0]*numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a]+=1
        
        queue=deque()
        for i in range(numCourses):
            if in_degree[i]==0:
                queue.append(i)

        count=0
        while queue:
            cur=queue.popleft()
            count+=1
            for course in graph[cur]:
                
                in_degree[course]-=1
                if in_degree[course]==0:
                    queue.append(course)
        return count==numCourses   
        