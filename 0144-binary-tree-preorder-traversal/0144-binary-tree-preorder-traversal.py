# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
    # def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # preorder Traversal
        # root --> left --> right
        # recursive solution
#         if not root:
#             return []
#         ans = []
#         def dfs(root):
#             if root:
#                 ans.append(root.val)
#                 dfs(root.left)
#                 dfs(root.right)
#         dfs(root)
#         return ans
        
        #Iterative solution
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        ans = []
        stack = []
        stack.append(root)
        
        while stack:
            node = stack.pop()
            if node: 
                ans.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
            
        return ans
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        