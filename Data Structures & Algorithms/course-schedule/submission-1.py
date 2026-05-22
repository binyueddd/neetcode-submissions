class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph={i:[] for i in range(numCourses)}
        for a,b in prerequisites:
            graph[a].append(b)

        
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            
            if not graph[course]:
                return True
            
            visited.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            graph[course]=[]
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True