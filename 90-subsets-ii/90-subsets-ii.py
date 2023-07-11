class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        def dfs(curr, nums):                          
            
            result.append(curr[:])

            if(len(nums) == 0):                                         
                return
            
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]: # we dont create duplicate initial branches.
                    continue
                dfs(curr + [nums[i]], nums[i+1:])  # we are sending, nums[i+1:] for next loop
                
        result = []
        dfs([], sorted(nums))                             
        return result
