class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        total_sum = sum(nums)
        curr = 0
        ans = []
        for item in nums:
            val = total_sum - curr - item
            total_sum -= item
            curr +=item
            ans.append(abs(val))

        return ans