class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        totalSum = sum(nums)
        currSum = 0
        for i,j in enumerate(nums):
            currSum += j
            if totalSum - currSum == currSum-j:
                return i
        return -1