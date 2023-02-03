class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # We know that how we got zigzag pattern
        # P     I    N
        # A   L S  I G
        # Y A   H R
        # P     I 
        
        # for first and last row, the next item is repeated a particular increment
        # increment = (numRows - 1) * 2
        # and for the mid rows the increment is decreasing by 2
        # so, it will be i + increment - 2*r
        # r == row number
        
        # base case 
        if numRows == 1:
            return s
        # Result
        res = ""
        
        for r in range(numRows):
            increment = 2*(numRows - 1) 
            for i in range(r, len(s), increment):
                res += s[i]
                if (r > 0 and r < numRows-1 and i + increment - 2*r < len(s)):
                    res += s[i + increment - 2*r]
        return res
                
        
        