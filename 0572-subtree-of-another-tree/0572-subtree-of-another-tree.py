# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if the "tree rooted at that node" is identical to the "tree rooted at subRoot".If we find such a node, we          can return true. If traversing the entire tree rooted at root doesn't yield any such node, we can return false.
        
        # Check for all subtree rooted at all nodes of tree "root"
        def dfs(root):
            
            # If this node is Empty, then no tree is rooted at this Node
            # Thus "tree rooted at node" cannot be same as "rooted at subRoot"
            # "tree rooted at subRoot" will always be non-empty (constraints)
            if root is None:
                return False
            elif isidentical(root,subRoot):
                return True 
            return dfs(root.left) or dfs(root.right)
        
        def isidentical(root1,root2):
            # if both roots are none, then it is identical otherwise not...         
            if not root1 and not root2:
                return True 
            elif not root1 or not root2:
                return False
            
            # if both are non empty then they sholud be identical recursively
            else:
                
                a = isidentical(root1.left,root2.left)
                b = isidentical(root1.right,root2.right)
                # ~ values of nodes are same
                # ~ left subtrees are identical
                # ~ right subtrees are identical
                
                if root1.val == root2.val and (a and b):
                    return True
                else:
                    return False
        return dfs(root)