class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        def odd(num):
            if num % 2 == 0:
                return False
            return True 
        
        if not odd(low) and not odd(high):
            return (high - low)//2
            
        elif odd(low) and odd(high):
            return ((high - low - 2 )//2) + 2
        
        else:
            if odd(low):
                return 1 + (high - low - 1)//2
            else:
                return 1 + (high - 1 - low)//2
            
      
