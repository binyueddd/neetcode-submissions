class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        path=[]
        nums.sort()
        n=len(nums)
    
        def dfs(i):
            if i==n:
                res.append(path[:])
                return
                # 正在决定第 i 个元素选不选。只有当：i == n，说明所有元素都已经决定完了。这时候 path 才是一个完整子集，所以才加入答案
            
            j=i
            while j<n and nums[j]==nums[i]:
                j+=1
            count=j-i

            dfs(j)

            for c in range(1,count+1):
                path.append(nums[i])
                dfs(j)
            
            for c in range(count):
                path.pop()
            

        dfs(0)
        return res