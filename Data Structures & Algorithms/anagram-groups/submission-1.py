class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for string in strs:
            key="".join(sorted(string))
            group[key].append(string)
        return list(group.values())