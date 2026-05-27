class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m=len(s1)
        n=len(s2)
        if m>n:
            return False

        need=[0]*26
        window = [0]*26
        for ch in s1:
            need[ord(ch)-ord("a")]+=1
        
        for i in range(m):
            window[ord(s2[i])-ord("a")]+=1
        
        if need==window:
            return True
        
        for end in range(m,n):
            start=end-m
            window[ord(s2[end])-ord("a")]+=1
            window[ord(s2[start])-ord("a")]-=1

            if window==need:
                return True
        
        return False

        

