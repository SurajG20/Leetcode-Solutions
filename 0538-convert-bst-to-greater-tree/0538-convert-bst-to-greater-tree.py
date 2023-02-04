# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #Iterative Stack Method
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [] # create a stack
        node = root # node is for iterating, we dont want to change root
        total = 0 # Total sum till now
        
        if not node: # if node doesnt exist
            return None
        
        while stack or node: # While stack has values and node exist
            
            while node: # we append the node till the rightmost
                stack.append(node)
                node = node.right

            node = stack.pop() # first we pop, we will have rightmost element 
            total += node.val # we add its value to total
            node.val = total # we change the value of node
            node = node.left # as we want to do reverse inorder
        
        return root
        

#     def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    
#         # We can do reverse Inorder Traversal, and Keep an currSum variable
#         # first we add currsum to root, then add root val to currsum
#         # Explaination between global and nonlocal
#           # tc = O(N) sc = O(N)
            
#         currSum = 0
#         def reverse(node):
#             nonlocal currSum   
            
#             if not node:
#                 return None
            
#             reverse(node.right)
#             temp = node.val
#             node.val += currSum
#             currSum += temp
#             reverse(node.left)
            
            
#         reverse(root)
#         return root
    
    
    # Must be some conceptual problem
    ### Dont know why it isnt working
#     def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:   
#         def s(node):
#             nonlocal total
            
#             if not node:
#                 return None
#             s(node.left)
#             total += node.val
#             s(node.right)
            
#         total = 0    
#         s(root)
#         print(total)
        
#         def inorder(node):
#             if not node:
#                 return None
#             inorder(node.left)
#             node.val,total = total, total - node.val
#             inorder(node.right)
            
#         inorder(root)
#         return root
        
            
        