"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
#     # we can not access childrens like pointers as in binary tree, we will iterate of each children
    
#     def preorder(self, root: 'Node') -> List[int]:
        
#         if not root:
#             # base case:
#             # empty node or empty tree
#             return []
        
#         else:
#             # general case:
#             path = []

#             # Travese current node with preorder:
#             path.append( root.val )
            
#             # Traverse children with preorder:
#             for child in root.children:
#                 path += self.preorder( child )
                
#             return path

    # Iterative solution.....
    def preorder(self, root: 'Node') -> List[int]:
        # base_case:
        traverse_stack = [root]
        path = []
        
        # general case:
        while traverse_stack:
            
            current = traverse_stack.pop()
            
            if current:
                
                # Travese current node with preorder:
                path.append( current.val )
                

                if not current.children:
                    continue
                
                
                # Traverse children with preorder:
                # Left part if of higher priority than right part.
                # Thus, push right part before left part.
                for i in range( len(current.children)-1, -1, -1 ):
                    traverse_stack.append( current.children[i] )
                
        return path
    
            
        