# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # TC-O(N2) SC- O(N) 
        # This recursive solution is quadratic time because for every item in array, we will call for max function
        
        if not nums: # Array is empty
            return None
        
        if len(nums) == 1: # Single element in the array
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
    
             
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        if not nums: # empty array 
            return None
        stk = [] # stack
        last = None # to keep track of last popped element
        
        for num in nums: # iterating over each element in nums
            
            while stk and stk[-1].val < num: # we check if the current element value is greater than last item in stack
                last = stk.pop()
                
            node = TreeNode(num) #Make the current element as a node
            
            if stk:
                stk[-1].right = node 
                
            if last:
                node.left = last
            stk.append(node)
            last = None
        return stk[0]
        