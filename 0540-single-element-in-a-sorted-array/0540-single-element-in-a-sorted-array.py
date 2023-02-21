class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        lo, hi = 0, len(nums)-1 # boundaries
        
        while lo < hi: # terminating condition
            mid = lo+(hi-lo)//2 # mid point
            
            if nums[mid] == nums[mid-1]:  # we found pair and it matches previous number
                
                if mid%2: # if the mid index is odd, means even number of elements are there 
                    lo = mid+1  # we search in right half
                    
                else: # if its even, odd elements are there before it. we need to go left side.
                    
                    hi = mid-2  
                    
            elif nums[mid] == nums[mid+1]: #the number after is same. 
                
                if mid%2: # index is odd, we need to go left side  
                    hi = mid-1 
                else: # else we need to right side         
                    lo = mid+2  
            else:  
                # else return the number
                return nums[mid]
            
        return nums[lo]