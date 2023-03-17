class Solution:
    def hammingWeight(self, n: int) -> int:
        # Think of a number in binary n = XXXXXX1000, n - 1 is XXXXXX0111. n & (n - 1) will be XXXXXX0000 which is just remove the last significant 1\
        
        
        res = 0
        
        while n:
            n = n & (n-1)
            res += 1
        return res