# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True 
        elif not p or not q:
            return False
        else:
            same = self.isSameTree
            a = same(p.left,q.left)
            b = same(p.right,q.right)
            if p.val == q.val and (a and b):
                return True
            
        