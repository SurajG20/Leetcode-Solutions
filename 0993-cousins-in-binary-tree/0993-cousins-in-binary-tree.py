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
    
class Solution:
    def isCousins(self, root, x, y):
        # our dfs function 
        def dfs(node, parent, depth, val):
            
            if not node: # base condition
                return
            
            if node.val == val: # if it is the desired node
                return depth, parent # we return the depth and parent
            
            # we recursively call for both left and right subtree
            # "OR" will give the desired value if it matches
            return dfs(node.left, node, depth + 1, val) or dfs(node.right, node, depth + 1, val)
        
        dep_x, par_x = dfs(root, None, 0, x) # we get the depth and parent for x 
        
        dep_y, par_y = dfs(root, None, 0, y) # we get the depth and parent for y

        
        # check for same depth and different parent 
        return dep_x == dep_y and par_x != par_y 