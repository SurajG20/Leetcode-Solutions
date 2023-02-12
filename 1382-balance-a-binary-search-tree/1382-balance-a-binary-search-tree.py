# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        # We do a inorder traversal to get the sorted array.
        def inorder(node):
            nonlocal arr
            if not node:
                return None
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
        
        arr = [] # Inorder Traversal
        
        inorder(root)
    
        def dfs(left,right): # We convert this sorted array to a binary search Tree
            
            if left > right:
                return None
            mid = (left + right)//2
            node = TreeNode(arr[mid])
            node.left = dfs(left,mid-1)
            node.right = dfs(mid+1,right)
            
            return node
        
        return dfs(0,len(arr)-1)

                