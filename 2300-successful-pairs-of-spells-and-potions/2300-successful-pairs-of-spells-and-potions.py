class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        potions.sort()
        
        def binaryFunction(arr,limit):
            
            left, right = 0,len(arr)
            while left < right:
                
                mid = left + (right - left) // 2
                if arr[mid]*limit >= success :
                    right = mid
                else:
                    left = mid + 1
                    
            return left

        
        res =[]
        
        for i in range(len(spells)):
            value = binaryFunction(potions,spells[i])
            print(value)
            res.append(len(potions)-value)
            
        return res
            
            
        
        
        
        
        
        
        
#         # brute force will not work
#         res = [0]*len(spells)
        
#         for i in range(len(spells)):
#             curr = spells[i]
#             count = 0
#             for val in potions:
#                 if curr*val>= success:
#                     count += 1
                    
#             res[i] = count
            
#         return res
                    
            