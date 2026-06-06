class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        path=[]
        n=len(nums)
        nums.sort()
        total=0

        def dfs(i,total):
            if total==target:
                res.append(path[:])
                return
            
            if total>target:
                return
            
            for j in range(i,n):
                if nums[j]+total>target:
                    break
                
                path.append(nums[j])
                dfs(j,total+nums[j])
                path.pop()
        dfs(0,0)
        return res
                
