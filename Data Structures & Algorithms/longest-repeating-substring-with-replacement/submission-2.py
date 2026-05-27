class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start=0
        longest=0
        count={}

        for end in range(len(s)):
            count[s[end]]=count.get(s[end],0)+1
            while (end-start+1)-max(count.values())>k:
                count[s[start]]-=1
                start+=1
            longest=max(longest,end-start+1)
        return longest