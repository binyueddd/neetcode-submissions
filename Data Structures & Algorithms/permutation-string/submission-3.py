class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m=len(s1)
        n=len(s2)
        if m>n:
            return False

        exits = defaultdict(int)
        for ch in s1:
            exits[ch]+=1
        
        window = defaultdict(int)
        for i in range(n):
            ch = s2[i]
            window[ch]+=1
            
            if i >= m:
                window[s2[i-m]] -=1
                if window[s2[i-m]]==0:
                    del window[s2[i-m]]
            
            if i>=m-1:
                if window==exits:
                    return True
        
        return False

            
        