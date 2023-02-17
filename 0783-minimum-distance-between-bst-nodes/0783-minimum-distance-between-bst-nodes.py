# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        pre = -float('inf') # previous node
        res =  float('inf') # current result

        def minDiffInBST(self, root):
            if root is None:
                return

            self.minDiffInBST(root.left) # search in left half
            # evaluate and set the current node as the node previously evaluated
            
            self.res = min(self.res, root.val - self.pre)
            
            self.pre = root.val # keep changing the previous value 

            self.minDiffInBST(root.right) # search in right half
            
            return self.res

        
        
        
        
        
        
        
        
#         inorder = [] # a list for inorder
        
#         def dfs(node): # Inorder Traversal
#             nonlocal inorder
#             if not node:
#                 return None
#             dfs(node.left)
#             inorder.append(node.val)
#             dfs(node.right)
            
#         dfs(root)

#         res = float(inf) # res
        
#         for i in range(len(inorder)):
#             for j in range(i+1,len(inorder)):
#                 res = min(res,inorder[j]-inorder[i])
                
#         return res
                