# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # We have binary search tree. Variable root is pointer to the tree root.
        # We have boundaries [L..R]
        # We need to trim our tree so that all elements fit into boundaries [L..R]
        
        # Time complexiy O(N)
        # Space complexity O(N)
        
        def dfs(node):
            if not node:
                return 
            if node.val > high:
                return dfs(node.left)
            if node.val < low:
                return dfs(node.right)
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            return node
        
        return dfs(root)
        