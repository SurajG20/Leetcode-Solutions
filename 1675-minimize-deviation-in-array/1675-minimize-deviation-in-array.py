import heapq
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        
        # if it is odd, multiply it by 2 and push it onto the heap. Otherwise, just push it onto the heap.
        pq = [-num*2 if num % 2 == 1 else -num for num in nums]
        
        # make the heap
        heapq.heapify(pq) 
        
        # Initialize a variable to keep track of the minimum value
        min_val = float('inf')
        
        # find the minimum value 
        for num in nums:
            min_val = min(min_val, num if num % 2 == 0 else num*2)
        
        # a variable to keep minimum deviation
        min_deviation = float('inf')
        
        # we iterate we do not break out of loop
        while True:
            max_val = -heapq.heappop(pq) # current max value 
            min_deviation = min(min_deviation, max_val - min_val) # find the minimum deviation
            
            if max_val % 2 == 1: # if it is odd, we break because we can not reduce it
                break
                
            max_val //= 2 # else we reduce it in half
            
            min_val = min(min_val, max_val) # find new min value 
            
            heapq.heappush(pq, -max_val) # we again push the new max value 
            
        return min_deviation
    
