class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n=len(tasks)
        new_tasks = sorted((enqueue,process,i) for i, (enqueue,process) in enumerate(tasks))

        heap=[]
        res=[]

        time = 0
        i=0

        while i<n or heap:
            if not heap and time<new_tasks[i][0]:
                time = new_tasks[i][0]
            
            while i < n and new_tasks[i][0]<=time:
                enqueue, process, index = new_tasks[i]
                heapq.heappush(heap, (process, index))
                i+=1
            
            process,index = heapq.heappop(heap)
            res.append(index)
            time+=process
    
        return res

