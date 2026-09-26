# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.maxDiameter = 0

        if not root:
            return 0

        def traverse(node):
            if not node:
                return 0

            left_height = traverse(node.left)
            right_height = traverse(node.right)

            self.maxDiameter = max(self.maxDiameter, left_height + right_height)

            return max(left_height, right_height) + 1
        
        traverse(root)

        return self.maxDiameter