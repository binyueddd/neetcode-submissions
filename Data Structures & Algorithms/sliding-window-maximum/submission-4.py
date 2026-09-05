class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=deque()
        res=[]

        for right in range(len(nums)):
            while q and nums[q[-1]] <= nums[right]:
                q.pop()
            
            q.append(right)

            if q[0]<right - k+1:
                q.popleft()
            
            if right >= k-1:
                res.append(nums[q[0]])
            
        return res