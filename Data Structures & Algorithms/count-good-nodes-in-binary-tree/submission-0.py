# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # A node is good if all of its parents values are less than itself
        def dfs(node, maxVal):
            if not node:
                return 0
            
            # Is current node good?
            if node.val >= maxVal:
                res = 1
            else:
                res = 0
            
            # Update max value for children
            maxVal = max(maxVal, node.val)

            # Sum current node + left subtree + right subtree
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)

            return res
        
        return dfs(root, root.val)
            
