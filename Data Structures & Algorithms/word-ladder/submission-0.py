class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet=set(wordList)
        if endWord not in wordSet:
            return 0
        
        queue=deque()
        queue.append((beginWord,1))

        visited=set()
        visited.add(beginWord)

        while queue:
            word,step=queue.popleft()

            if word==endWord:
                return step
            
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    newword=word[:i]+ch+word[i+1:]

                    if newword not in visited and newword in wordSet:
                        visited.add(newword)
                        queue.append((newword,step+1))
            
        return 0