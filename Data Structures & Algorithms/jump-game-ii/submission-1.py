class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        farthest=0
        cur_end=0
        step=0
        for i in range(n-1):
            farthest=max(farthest,nums[i]+i)
            if i==cur_end:
                step+=1
                cur_end=farthest
        return step