class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        path=[]
        nums.sort()
        n=len(nums)

        def dfs(i):
            res.append(path[:])
            # 当前 path 已经是一个合法子集，接下来可以从 i 之后继续追加元素。
            if i==n:
                return
            
            for j in range(i,n):
                if j>i and nums[j]==nums[j-1]:
                    continue
                
                path.append(nums[j])
                dfs(j+1)
                path.pop()
            
        dfs(0)
        return res