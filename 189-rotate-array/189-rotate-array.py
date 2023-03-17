class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # "we will reverse the P1 first which become [4,3,2,1] & then we reverse P2 which becomes [7,6,5]. Now finally what           we have to do is we gonna reverse the complete array "
        
        # reverse function
        def reverse(nums,start,end):
            while start < end:
                nums[start],nums[end] = nums[end],nums[start]
                start += 1
                end -= 1
        
        # base condition
        if k is None or k <= 0:
            return 
        
        # if k is larger than the array, we can take modulo
        k = k % len(nums)
        
        end = len(nums) - 1
        
        reverse(nums, 0, end - k)
        reverse(nums, end - k + 1, end)
        reverse(nums, 0, end)
        
        return nums