# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # We know that the longest path does not have to pass through the root, hence we need to find the logest path or curve corresponding each node 
        # We can keep an non local variable to keep track of maximum path of each node 
        
        
        def depth(root):
            # When we recall the funtion we do not have to keep puting the variable in fun again again...
            nonlocal max_length
            
            if root == None:
                return 0
            left = depth(root.left)
            right = depth(root.right) 
            
            max_length = max(max_length, left + right)
            return 1 + max(left,right)
            
        max_length = 0
        depth(root)
        return max_length