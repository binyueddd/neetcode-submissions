class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph={}    # 需要避免重复边
        indegree = {}

        for word in words:
            for ch in word:
                if ch not in graph:
                    graph[ch]=set()
                if ch not in indegree:
                    indegree[ch]=0
                
        for i in range(len(words)-1):
            word1=words[i]
            word2=words[i+1]
            
            if len(word1)>len(word2) and word1.startswith(word2):
                return ""

            min_length=min(len(word1),len(word2))

            for j in range(min_length):
                if word1[j]!=word2[j]:
                    if word2[j] not in graph[word1[j]]:
                        graph[word1[j]].add(word2[j])
                        indegree[word2[j]]+=1
                    break
        
        queue=deque()
        for ch in indegree:
            if indegree[ch]==0:
                queue.append(ch)
        
        res=[]
        while queue:
            cur=queue.popleft()
            res.append(cur)
            for nxt in graph[cur]:
                indegree[nxt]-=1
                if indegree[nxt]==0:
                    queue.append(nxt)
        
        if len(res)!=len(indegree):
            return ""
    
        return "".join(res)

