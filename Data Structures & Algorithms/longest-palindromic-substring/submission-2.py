class Solution:
    def longestPalindrome(self, s: str) -> str:
        def ispali(left,right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            
            return s[left+1:right]

        res=""
        for i in range(len(s)):
            odd=ispali(i,i)
            if len(odd)>len(res):
                res=odd
            
            even=ispali(i,i+1)
            if len(even)>len(res):
                res=even
        return res