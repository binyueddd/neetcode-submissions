class Solution:
    def countSubstrings(self, s: str) -> int:
        def ispalin(left,right):
            count = 0
            while left>=0 and right<len(s) and s[left]==s[right]:
                count+=1
                right+=1
                left-=1
            
            return count
        
        res = 0
        for i in range(len(s)):
            res += ispalin(i,i)
            res += ispalin(i,i+1)
        
        return res
