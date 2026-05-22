# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.step=0
        self.result=None
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.step+=1
            if self.step==k:
                self.result=node.val
                return
            
            dfs(node.right)
        dfs(root)

        return self.result
            