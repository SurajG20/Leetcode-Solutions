class Solution:
    # '''''' recursive but using cache decorator''''''
#     @cache
#     def climbStairs(self, n: int) -> int:          
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
#         return self.climbStairs(n-1) + self.climbStairs(n-2)
    
    
    # ''''''    using memoization      ''''''
#     def climbStairs(self, n: int) -> int: 
#         def climb(n):
#             if n in memo: # memo to store result of sub problem
#                 return memo[n] # checking if n present in memo 
#             else:
#                 memo[n] = climb(n-1) + climb(n-2) # if not then store the value there
#                 return memo[n] # and return it 
                
#         memo = {1:1,2:2}     
#         return climb(n)

       # '''''' using dynamic programming ''''''
    # https://leetcode.com/problems/climbing-stairs/solutions/2905464/o-n-o-1-python-solution-explained/
    def climbStairs(self, n: int) -> int:
        
        # Fibonacci Sequence starting value
        one_step, two_steps = 1,1
        
        # traverse from the top
        for i in range(n-1):
            
            # Since we don't want to add two values for our two_steps
            # because we only want to shift our two_steps variable where one_step was orginally as 
            # So, before updating our one_step variable, we store the orginal one-step value in temp 
            temp = one_step
            
            # add two previous values
            one_step = one_step + two_steps
            
            # just shift two_steps variable to where one_step was at previously
            two_steps = temp
            
        # Once one_step variable reaches 0, we now have our different ways values
        return one_step            