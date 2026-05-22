class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        same=defaultdict(int)
        if len(s)!=len(t):
            return False
        for ch in s:
            same[ch]+=1
        
        for ch in t:
            same[ch]-=1
            if same[ch]<0:
                return False

        return True
