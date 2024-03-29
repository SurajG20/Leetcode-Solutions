class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # We initialize two pointers i = 0, j = 0. Iterate j over range(len(nums)), and if nums[j] != 0, we swap nums[i] and nums[j], and increment i by 1. It is easy to see the loop invariant that nums[:i+1] contains all nonzero elements in nums[:j+1] with relative order preserved. Hence when j reaches len(nums)-1, nums[:i+1] contains all nonzero elements in nums with relative order preserved.
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
        return nums
#         for i,val in enumerate(nums):
#             if val == 0:
#                 nums.remove(val)
#                 nums.append(val)
#         return nums
            