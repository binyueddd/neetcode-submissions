class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occur = defaultdict(int)
        start = 0
        end = 0
        if not s:
            return 0
        
        longest = 0
        while end<len(s):
            occur[s[end]]+=1
            while occur[s[end]]>1:
                occur[s[start]]-=1
                start+=1
            end+=1
            longest=max(longest,end-start)
        return longest

