# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return

        global_max = root.val

        def dfs(node):
            nonlocal global_max

            if not node:
                return 0
            
            left_gain = dfs(node.left)
            right_gain = dfs(node.right)

            value = node.val + left_gain + right_gain
            global_max = max(global_max, value)

            return max(0, node.val + left_gain, node.val + right_gain)
        
        dfs(root)
        return global_max