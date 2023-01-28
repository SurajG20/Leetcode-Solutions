# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursive solution
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        merged = TreeNode()
        
        if not root1 and not root2:
            return None
        elif not root1:
            return root2
        elif not root2:
            return root1
        else:
            merged.val = root1.val + root2.val
            merged.left  = self.mergeTrees(root1.left,root2.left)
            merged.right = self.mergeTrees(root1.right,root2.right)
            
        return merged
    
#     # We are not creating a new Tree here....
#     def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
#         if not root1:
#             return root2
#         if not root2:
#             return root1

#         root1.val += root2.val
        
#         root1.left = self.mergeTrees(root1.left, root2.left)
#         root1.right = self.mergeTrees(root1.right, root2.right)
#         return root1
    
    # Iterative solution
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # We are actually changing the root1 Tree
        if not t1 or not t2: 
            return t1 or t2
        # appending the roots in stack
        s = [(t1, t2)]
        
        while s: 
            # we pop the item 
            n1, n2 = s.pop()
            
            #nothing to add on
            if not n2:
                continue
            # else append the values
            n1.val += n2.val
            if not n1.right: 
                n1.right = n2.right
            else: 
                s.append((n1.right, n2.right))
            if not n1.left: 
                n1.left = n2.left
            else: 
                s.append((n1.left, n2.left))
        return t1
    
    
        