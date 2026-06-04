# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.pre = None

        def inorder(node):
            if not node:
                return True

            if not inorder(node.left):
                return False

            if self.pre and self.pre.val >= node.val:
                return False

            self.pre = node

            return inorder(node.right)

        return inorder(root)