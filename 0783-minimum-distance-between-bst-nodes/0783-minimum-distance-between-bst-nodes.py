# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        inorder = [] # a list for inorder
        
        def dfs(node): # Inorder Traversal
            nonlocal inorder
            if not node:
                return None
            dfs(node.left)
            inorder.append(node.val)
            dfs(node.right)
            
        dfs(root)

        res = float(inf) # res
        
        for i in range(len(inorder)):
            for j in range(i+1,len(inorder)):
                res = min(res,inorder[j]-inorder[i])
                
        return res
                