# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        def max_binary(nums):
            if not nums:
                return None
            print("nums",nums)
            ele = max(nums)
            
            print("ele",ele)
            x = nums.index(ele)
            
            print("x",x)
            Node = TreeNode(ele)
            Node.left = max_binary(nums[:x])
            Node.right = max_binary(nums[x+1:])
            
            return Node
        
        return max_binary(nums)
         
        