class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for i,val in enumerate(numbers):
            if val in hashmap:
                return [hashmap[val]+1,i+1]
            else:
                hashmap[target-val] = i
        
            