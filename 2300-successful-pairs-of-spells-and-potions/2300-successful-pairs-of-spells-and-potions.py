class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        # sort the potions array
        potions.sort()
        
        
        # binary function 
        def binaryFunction(arr,limit):
            
            left, right = 0,len(arr) # low and high
            
            while left < right:
                
                mid = left + (right - left) // 2 # middle element 
                
                # finding the lowest number which satisfy the condition
                if arr[mid]*limit >= success :
                    right = mid
                else:
                    left = mid + 1
                    
            return left

        
        res =[]
        
        for i in range(len(spells)):
            value = binaryFunction(potions,spells[i])
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
                    
            