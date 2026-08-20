# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        seen = set()
        res = []

        def dfs(node, level):
            nonlocal res

            if not node:
                return None
            
            if level not in seen:
                res.append(node.val)
                seen.add(level)
            
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
            return
        
        dfs(root, 0)
        
        return res
            
