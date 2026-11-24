class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache={}
        def dfs(i,total):
            if total== amount:
                return 1
            if total > amount or i>len(coins)-1:
                return 0
            if (i,total) in cache:
                return cache[(i,total)]

            skip = dfs(i+1, total)
            keep = dfs(i, total+coins[i])

            count = skip+keep
            cache[(i,total)]=count
            return count
        
        return dfs(0,0)
            

