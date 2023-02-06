# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:     
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        #  We want to delete a node      
        #  iF node is not found, we return the same root 
        # iF node is found, 
                    # 1. If it is leaf node...we remove it 
                    # 2. If it is in middle, we replace it with inorder successor, and delete successor
        
        if root is None: # empty node
            return None
        elif root.val > key: # key less than root
            root.left = self.deleteNode(root.left,key)
        elif root.val < key: # key greater than root
            root.right = self.deleteNode(root.right,key)
        else: # root has same value as key
            
            if not root.left: # if root's left is empty
                return root.right
            
            elif not root.right: # if root's right is empty
                return root.left
            
            else: 
                # if it has both root, we can replace with greater or lesser value
                # we are doing inorder successor 
                succ = self.Succ(root.right)
                root.val = succ
                root.right = self.deleteNode(root.right,succ)

        return root
    
    def Succ(self,curr):
        while curr.left:
            curr = curr.left
        return curr.val
                