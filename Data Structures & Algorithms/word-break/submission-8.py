class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        cache={}
        def dfs(end, word):
            if end==n:
                return word==""
            
            key=(end,word)
            if key in cache:
                return cache[key]

            word+=s[end]
            if word in wordDict and dfs(end+1,""):
                cache[key]=True
                return True
            
            cache[key]=dfs(end+1,word)
        
            return cache[key]
        return dfs(0,"")
