# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # What we need to do here is just to traverse our tree, using dfs and check balance for every node.
        # dfs(node) here returns depth of subtree with root in node. If it is None, depths is equal to 0. 
        # We evaluate depths of left and right subtee and return maximum of them plus one. 
        # Also we check balance and if absolute difference is more than 1, we can mark variable self.Bal as False:
        # we can state now that tree is not balanced.
        # TC = O(N)
        # SC = O(H)
        self.flag = True 
        def dfs(root):
            if not root:
                return 0
            L = dfs(root.left)
            R = dfs(root.right)
            if abs(L-R) > 1:
                self.flag = False
            return max(L,R) + 1
        
        
        dfs(root)
        return self.flag
                