class NumArray:
    def __init__(self, nums: List[int]):
        
        self.preSum = nums  # pass by pointer!
        
        for i in range(len(nums)-1):
            self.preSum[i+1] += self.preSum[i]

    def sumRange(self, left: int, right: int) -> int:
        # we need to skip 0th item
        if left == 0: return self.preSum[right]
        return self.preSum[right] - self.preSum[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)