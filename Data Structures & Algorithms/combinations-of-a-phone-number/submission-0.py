MAPPING={
    2:"abc",
    3:"def",
    4:"ghi",
    5:"jkl",
    6:"mno",
    7:"pqrs",
    8:"tuv",
    9:"wxyz"
}
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res=[]
        path=[]
        n=len(digits)

        def dfs(i):
            if len(path)==n:
                res.append("".join(path))
                return
            
            digit=digits[i]
            letters=MAPPING[int(digit)]
            for ch in letters:
                path.append(ch)
                dfs(i+1)
                path.pop()
        
        dfs(0)
        return res
