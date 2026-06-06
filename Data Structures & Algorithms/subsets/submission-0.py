class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        path=[]
        n=len(nums)

        def dfs(start):
            if start==n:
                res.append(path[:])
                return 
            
            dfs(start+1)

            path.append(nums[start])
            dfs(start+1)
            path.pop()
        
        dfs(0)
        return res