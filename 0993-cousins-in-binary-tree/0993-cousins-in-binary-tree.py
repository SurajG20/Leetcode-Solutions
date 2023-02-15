# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = [(root,None)] # add node & parent as tuple
        
        while q:
            
            temp = [] # to keep track of another layer
            
            # intialise both parent as None
            xpar = None 
            ypar = None
            
            # we check for each pair
            for node, parent in q:
                if node.val == x:
                    xpar = parent
                elif node.val == y:
                    ypar = parent
                
                # if both parent have some value, we chck if they are different
                if xpar and ypar:
                    return xpar != ypar
                # append both left and right children
                if node.left:
                    temp.append((node.left,node))
                if node.right:
                    temp.append((node.right,node))
            q = temp
            
        return False
    
        
# class Solution:
#     def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
#         self.xDepth = -1
#         self.yDepth = -2
#         self.xParent = None
#         self.yParent = None

#         def dfs(root, parent, x, y, depth):
#             if root is None: return
#             if root.val == x:
#                 self.xParent = parent
#                 self.xDepth = depth
#             elif root.val == y:
#                 self.yParent = parent
#                 self.yDepth = depth
#             else:
#                 dfs(root.left, root, x, y, depth+1)
#                 dfs(root.right, root, x, y, depth+1)

#         dfs(root, None, x, y, 0)
#         return self.xDepth == self.yDepth and self.xParent != self.yParent        
        
        
        
        