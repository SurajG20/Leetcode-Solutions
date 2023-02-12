# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        # base condition
        if not preorder:
            return None
        # Initiate the Node
        node = TreeNode(preorder[0])
        
        # Now we go till we find greater value than our root values
        i = 1
        
        while i < len(preorder) and preorder[i] < node.val:
            i += 1
            
        node.left = self.bstFromPreorder(preorder[1:i])
        node.right = self.bstFromPreorder(preorder[i:])
        
        return node
        
     
#       # We can do this way, it will create a different BST
#         preorder.sort()
#         def helper(l,r):
            
#             if l > r:
#                 return None
            
#             mid = (l+r)//2
#             node = TreeNode(preorder[mid])
#             node.left = helper(l,mid-1)
#             node.right = helper(mid+1,r)
            
#             return node
        
#         return helper(0,len(preorder)-1)
        