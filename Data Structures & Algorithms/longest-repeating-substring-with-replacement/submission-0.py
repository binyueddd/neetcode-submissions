class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count=defaultdict(int)
        start=0
        longest=0
        max_freq=0
        for end in range(len(s)):
            count[s[end]]+=1
            max_freq=max(max_freq, count[s[end]])

            while end-start+1-max_freq>k:
                count[s[start]]-=1
                start+=1
            
            longest = max(longest,end-start+1)
        return longest
            
            
            