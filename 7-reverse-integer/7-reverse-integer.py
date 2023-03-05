class Solution:
    def reverse(self, x: int) -> int:
        if 0 <= x < 10:
            return x
        
        if x >= 2**31-1 or x <= -2**31:
            return 0
        
        res  = ""
        
        if x > 0:
            while x:
                res += str(x%10)
                x = x // 10
             
        else:
            
            x = abs(x)
            while x:
                res += str(x%10)
                x = x // 10
            res = "-" + res
                
        if int(res) >= 2**31-1 or int(res) <= -2**31:
            return 0
        else: 
            return int(res)
            
        
#         if x < 0:
#             s = str(abs(x))
#             s = s[::-1]
#             return -int(s)
#         else:
#             s = str(abs(x))
#             s = s[::-1]
#             return int(s)
            
        
        