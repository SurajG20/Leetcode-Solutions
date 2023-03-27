class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        a = 1
        b = 0
        res = 0
        for i in range(2,n+1):
            res = a + b
            b = a
            a = res
        return res