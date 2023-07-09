class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        count = 0
        n  = 0
        while n < len(nums):
            if nums[n] == 1:
                count += 1
            else:
                count = 0
            maxCount = max(maxCount, count)
            n += 1
        return maxCount