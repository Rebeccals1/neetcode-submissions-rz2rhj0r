# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if both are empty, return true
        if not p and not q:
            return True
        
        # If one is empty and the other isn't, return false
        if not p or not q:
            return False
        
        # If both are not empty and are not equal
        if p.val != q.val:
            return False
        
        # Recursive step, check all nodes
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        # Returns true or false
        return (left and right)
