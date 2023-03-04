class Solution:
    def coloredCells(self, n: int) -> int:
        
        if n == 1:
            return 1
        
        OddNum = 1
        for i in range(n-1):
            OddNum += 2
            
        total = OddNum*OddNum
        
        return (total +1 )//2
            
        