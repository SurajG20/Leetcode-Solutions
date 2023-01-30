# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Height of a tree
        # 1. find the height of left subtree
        # 2. find the height of right subtree
        # 3. max(left,right) + 1
        depth = 0
        if not root:
            return 0
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        depth = max(left_height,right_height) + 1
        
        return depth
            
        