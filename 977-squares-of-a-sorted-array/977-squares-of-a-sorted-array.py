class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]: 
        res = [0]*len(nums) # result array
        l = 0 # left pointer
        r = len(nums) - 1 # right pointer

        # iterating over the result array in reverse order
        # and comparing each element using two pointers and incrementing them as usage
        for i in range(len(nums)-1,-1,-1): 
            if abs(nums[l]) > abs(nums[r]):  
                res[i] = nums[l]*nums[l]
                l += 1
            else:
                res[i] = nums[r]*nums[r]
                r -= 1
        return res


        