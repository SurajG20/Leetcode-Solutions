# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode': 
        # Recursive Solution
        #TC = O(H) SC= O(H)
        # We keep iterate root in our BST:
        # If root.val > p.val and q.val then both node p and q belong to the left subtree, search in left side.
        # If root.val < p.val and q.val then both node p and q belong to the right subtree,search in right side.
        # Now, small <= root.val <= large the current root is the LCA between q and p.
        
        large = max(p.val,q.val)
        small = min(p.val,q.val)
        
        if not root or not p or not q:
            return None
        elif large < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif small > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root
        
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #Iterative solution
        
        small = min(p.val, q.val)
        large = max(p.val, q.val)
        
        while root:
            if root.val > large:  # p, q belong to the left subtree
                root = root.left
            elif root.val < small:  # p, q belong to the right subtree
                root = root.right
            else:  # Now, small <= root.val <= large -> This is the LCA between p and q
                return root
        return None
