# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # As for the bfs, lever order iteration
        # We need queue implemented using collections
        q = collections.deque()
        
        # Result
        res = []
        # First we append the root 
        q.append(root)
        
        # Corner case
        if not root:
            return [] 
        
        while q:
            temp = [] # A list that reset for each level
            
            for i in range(len(q)): # Keep adding element of a particular level
                node = q.popleft()
                
                temp.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)  
                    
            res.append(temp)
            
        return res
        
        