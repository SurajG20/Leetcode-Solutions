# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         if not root:
#             return None
#         data1 = []
#         data2 = []
#         return self.inorderT(root,data1) == self.reverseT(root,data2)
#     # Inorder Traversal        
#     def inorderT(self,root,nums):
#         if root != None:
#             self.inorderT(root.left,nums)
#             nums.append(root.val)
#             self.inorderT(root.right,nums)
#         return nums
#     # Reverse Traversal
#     def reverseT(self,root,nums):
#         if root != None:
#             self.reverseT(root.right,nums)
#             nums.append(root.val)
#             self.reverseT(root.left,nums)
#         return nums

class Solution:
    # Recursive solution
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.traverse(root.left,root.right)
    
    def traverse(self,left,right):
        # If left and right exists
        if left and right: 
            # Using a mirror example
            a=self.traverse(left.left,right.right)
            b=self.traverse(left.right,right.left)

            # This childrens will give Either True or False
            # Also the value of nodes should have same values
            if left.val == right.val and (a and b):
                return True
            else: 
                return False
        # Either one of them is None
        elif (left and (not right)) or (right and (not left)):
            return False
        # If both are None, then there is no value
        else:
            return True