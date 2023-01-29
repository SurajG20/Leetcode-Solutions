# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = [] # result
        count = defaultdict(int) # to keep count of level
        s = defaultdict(int) # to keep count of sum at corresponding level
        
        def dfs(node,i):
            if node: # If node exhits
                s[i] += node.val # add the value of ith key 
                
                count[i] += 1 # increase the count
                dfs(node.left,i+1) # call the dfs on left subtree
                dfs(node.right,i+1) # on the right subtree
        
        dfs(root,0)
        
        for i in range(len(s)):
            res.append(s[i]/count[i])
        return res
        
             
#         # Create a quque for BFS and apppend the root 
#         q = collections.deque()
#         q.append(root)        
#         # Result 
#         result = [] 
#         while q:
#             qlen = len(q) # How many elements on current level
#             temp = 0 # Sum at current level
            
#             # We are iterating each element at current level
#             for i in range(qlen):   
                
#                 node = q.popleft()
#                 temp += node.val
#                 if node.left:
#                     q.append(node.left) 
#                 if node.right:
#                     q.append(node.right) 
                    
#             result.append(temp/qlen)# Calculate the average
            
#         return result
    
            
            

            
            
            
        