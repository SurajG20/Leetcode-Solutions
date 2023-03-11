# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Use recursion. Pass down two parameters: 
        # 1. high (which means that all nodes in the the current subtree must be smaller than this value) 
        # 2. and low (all must be larger than it).
        # Compare root of the current subtree with these two values. 
        # Then, recursively check the left and right subtree of the current one.
        # Take care of the values passed down
        
        # Basically:
        # [1] with each pass, we set [MIN, MAX] threshold for the next node
        # [2] and check if the node is outside its bounds 
        
        def traverse(root, low, high):
            if not root:
                return True
            
            elif not low < root.val < high:
                return False
            
            return traverse(root.left,low, root.val) and traverse(root.right,root.val, high)
        
        return traverse(root,low=float('-inf'), high=float('inf'))