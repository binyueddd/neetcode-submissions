# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.res=float('-inf')
        def dfs(node):
            if not node:
                return 0
            left_max = max(0,dfs(node.left))
            right_max= max(0, dfs(node.right))

            cur_path_sum=node.val+left_max+right_max
            self.res = max(self.res, cur_path_sum)

            return node.val+max(left_max,right_max)
        
        dfs(root)
        return self.res
            
            
