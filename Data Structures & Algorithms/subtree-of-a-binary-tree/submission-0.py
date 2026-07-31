# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base Case: Empty root can't have a subtree
        if not root:
            return False
        
        # Check left and right subtrees to start matching
        if self.isSameTree(root, subRoot):
            return True

        # Recurse on left and right children
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        
        return left or right

    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Both are empty
        if not root and not subRoot:
            return True
        
        # If one is empty, they arent the same
        if not root or not subRoot:
            return False
        
        if root.val != subRoot.val:
            return False

        left = self.isSameTree(root.left, subRoot.left)
        right = self.isSameTree(root.right, subRoot.right)

        return left and right
            
            
            
