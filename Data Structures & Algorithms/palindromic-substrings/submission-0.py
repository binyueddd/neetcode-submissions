class Solution:
    def countSubstrings(self, s: str) -> int:
        def ispali(left,right):
            count=0
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
                count+=1
            return count
        
        res=0
        for i in range(len(s)):
            res+=ispali(i,i)
            res+=ispali(i,i+1)
        return res
