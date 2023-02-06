class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        i = 0
        j = n
        while i < n:
            res.append(nums[i])
            res.append(nums[n+i])
            i += 1
        return res
        