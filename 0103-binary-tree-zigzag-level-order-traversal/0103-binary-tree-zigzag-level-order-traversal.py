# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        
        q = collections.deque([root])
        
        res = []
        level = 0
        while q:
            
            temp = []
            for i in range(len(q)):
                
                node = q.popleft()
                temp.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if level % 2 == 0:
                res.append(temp)
            else:
                res.append(temp[::-1])
            level += 1
        return res