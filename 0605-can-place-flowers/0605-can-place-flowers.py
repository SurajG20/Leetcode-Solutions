# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # # Here we are creating a new array, hence the SC will be O(N)
        # f = [0] + flowerbed + [0]
        # for i in range(1,len(flowerbed)):
        #     if f[i-1] == 0 and f[i] == 0 and f[i+1] == 0:
        #         f[i] = 1
        #         n -= 1
        # return n >= 0
    
    
    
        
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # We can avoid the work of creating a new array by just some statements
        
        def bed(idx):
            # If the idx is -1 means we are checking the 0 element, we can the previous element as zero 
            # Similarly for last index, means we are checking for last element
            if idx == -1 or idx == len(flowerbed):
                return 0
            else:
                # If the both condition is not followed 
                return flowerbed[idx]
        # Length of flowerbed
        s = len(flowerbed)
        
        # count for number of suitable space
        cnt = 0
        
        for i in range(0, s): # Iterating over the list of flowerbed
            if bed(i-1) == bed(i) == bed(i+1) == 0: # Finding three consecutive zeroes
                flowerbed[i] = 1
                cnt +=1
            # If the count is greater than n, means we have sufficient space  
            if cnt >= n:
                return True
        return False