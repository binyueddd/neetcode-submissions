from functools import cache
class Solution:
    def checkValidString(self, s: str) -> bool:
        n=len(s)
        @cache
        def dfs(i,opencount):
            if opencount<0:
                return False
            if i==n:
                return opencount==0

            if s[i]=="(":
                return dfs(i+1,opencount+1)
            
            if s[i]==")":
                return dfs(i+1,opencount-1)
            
            if s[i]=="*":
                return dfs(i+1,opencount+1) or dfs(i+1,opencount-1) or dfs(i+1,opencount)
        
        return dfs(0,0)
