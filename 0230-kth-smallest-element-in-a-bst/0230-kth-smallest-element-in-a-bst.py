# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         # Recursive Inorder Traversal
#         # one way to solve this problem is do inorder traversal and find the (k-1)th element 
#         # TC = O(N)
#         # SC = O(N) N= total no. of nodes
        
#         def dfs(node):
#             nonlocal res
#             if not node:
#                 return None
#             dfs(node.left)
#             res.append(node.val)
#             dfs(node.right)
            
#         res = []
#         dfs(root)
        
#         return res[k-1]
    
    
class Solution:
    def kthSmallest(self, root, k):
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right
        