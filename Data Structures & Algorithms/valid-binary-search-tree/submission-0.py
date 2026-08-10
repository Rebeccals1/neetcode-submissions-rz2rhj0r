# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(node, left, right):
            if not node:
                return True

            # node.val must be strictly between left (lower bound) and right (upper bound)
            if not (left < node.val < right):
                return False
            
            valid_left = valid(node.left, left, node.val)
            valid_right = valid(node.right, node.val, right)

            return valid_left and valid_right
        
        return valid(root, float("-inf"), float("inf"))
            