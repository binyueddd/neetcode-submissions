class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        path=[]

        def backtracking(start, sum):
            if sum==target:
                res.append(path[:])
                return 
            
            if sum>target:
                return
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                sum+=nums[i]
                backtracking(i, sum)
                sum-=nums[i]
                path.pop()
        backtracking(0,0)
        return res
