class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        def ispalin(left,right):
            count=0
            while left>=0 and right<n and s[left]==s[right]:
                left-=1
                right+=1
                count+=1
            
            return count

        res=0
        for i in range(n):
            res+=ispalin(i,i)
            res+=ispalin(i,i+1)
        return res