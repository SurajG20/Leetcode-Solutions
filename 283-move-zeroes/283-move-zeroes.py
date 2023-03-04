class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i,val in enumerate(nums):
            if val == 0:
                nums.remove(val)
                nums.append(val)
        return nums
            