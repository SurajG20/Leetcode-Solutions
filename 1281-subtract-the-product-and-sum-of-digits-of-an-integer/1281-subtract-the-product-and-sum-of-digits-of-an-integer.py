class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        string = str(n)
        S = 0
        P = 1
        for i in string:
            S += int(i)
            P *= int(i)
        return P - S