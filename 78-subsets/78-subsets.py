class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = set()
        
        def dfs(i, subset):
            res.add(tuple(subset))
            if i == len(nums):
                return 
            
            dfs(i+1, subset + [nums[i]])
            
            dfs(i+1, subset)
            
        dfs(0,[])
        return res
            
            