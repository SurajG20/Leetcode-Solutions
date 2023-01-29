# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        # result  -- # stack
        res, stack = [], []
        
        # while we donot return, untill there is item in stack
        while True:
            
            # We first add all items in stack till we reach leftmost
            while root:
                stack.append(root)
                root = root.left
            # We return when the stack become empty, also exit the loop 
            if not stack:
                return res
            
            node = stack.pop()   # 1. First pop the leftmost item
            res.append(node.val) # 2. Then append it to res
            root = node.right    # 3. Check if it has any right attribute
            
 
        
        # Recursive solution
        # res = []
        # def dfs(root):
        #     if root:
        #         dfs(root.left)
        #         res.append(root.val)
        #         dfs(root.right)
        # dfs(root)
        # return res
                

            
            
            
        