class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left=0
        count = 0
        for i, ch in enumerate(s):
            while ch in window:
                window.remove(s[left])
                left += 1
            
            window.add(ch)
            count = max(count, i-left+1)
        
        return count