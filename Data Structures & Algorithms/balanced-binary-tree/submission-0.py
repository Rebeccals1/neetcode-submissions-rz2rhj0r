# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            # empty trees have a height of 0
            if not root:
                return 0
            
            # Left subtree is inbalanced
            left = dfs(root.left)
            if left == -1:
                return -1
            
            # right subtree is inbalanced
            right = dfs(root.right)
            if right == -1:
                return -1
            
            if abs(left - right) > 1:
                return -1 # Current node is inbalanced

            height = 1 + max(left, right)
            
            return height
        
        return dfs(root) != -1
