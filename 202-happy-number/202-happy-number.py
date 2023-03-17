class Solution:
    def isHappy(self, n: int) -> bool:
        def sqr(num):
            return sum(int(M)**2 for M in str(num))

        
        mapp = set()
        
        while n != 1:
            if n in mapp:
                return False
            mapp.add(n)
            n = sqr(n)
        return True