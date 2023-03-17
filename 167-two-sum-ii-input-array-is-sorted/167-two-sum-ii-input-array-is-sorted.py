class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        
        while l < r:
            total = numbers[l]+numbers[r]
            
            if total == target:
                return [l+1,r+1]
            elif total < target:
                l += 1
            else:
                r -= 1
            
        
#         hashmap = {}
        
#         for i,val in enumerate(numbers):
#             if val in hashmap:
#                 return [hashmap[val]+1,i+1]
#             else:
#                 hashmap[target-val] = i
        
            