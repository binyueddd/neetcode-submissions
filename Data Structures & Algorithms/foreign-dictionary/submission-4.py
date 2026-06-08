class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph=defaultdict(set)
        indegree={}

        for word in words:
            for ch in word:
                if ch not in graph:
                    graph[ch]=set()
                    indegree[ch]=0
                

        for i in range(len(words)-1):
            w1=words[i]
            w2=words[i+1]

            if len(w2)<len(w1) and w1[:len(w2)]==w2:
                return ""
            
            min_len=min(len(w1),len(w2))
            for j in range(min_len):
                if w1[j]!=w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        indegree[w2[j]]+=1
                    break
                
        queue=deque()
        
        for ch in graph:
            if indegree[ch]==0:
                queue.append(ch)
        
        res=[]

        while queue:
            cur=queue.popleft()
            res.append(cur)
            for nbr in graph[cur]:
                indegree[nbr]-=1
                if indegree[nbr]==0:
                    queue.append(nbr)
            
        if len(res)!=len(indegree):
            return ""
        
        return "".join(res)

        