# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # we can do bfs search, and keep track of a particular level and keep appending the last element in result array
        res = [] # result
        
        if not root: # if root exhits
            return res
        
        queue = collections.deque([root]) # a queue to implement bfs search
        
        while queue: # while there is element in queue
            
            res.append(queue[-1].val) # first we append last element of queue
            
            for i in range(len(queue)): # at each level, we pop from front and also add it children
                
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return res # return res
            
            