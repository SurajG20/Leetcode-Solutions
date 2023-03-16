class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #creating a dict to store the differences for easier access
        prev_val = {} 

        #using enumerate to iterate over the list
        for i,value in enumerate(nums): 

            #finding the diff we need to check for.
            another = target - nums[i]  

            #if it is present in the our data, then use it.
            if another in prev_val:
                return prev_val.get(another), i
                
            #otherwise store the value in the data
            else:
                prev_val[nums[i]] = i

