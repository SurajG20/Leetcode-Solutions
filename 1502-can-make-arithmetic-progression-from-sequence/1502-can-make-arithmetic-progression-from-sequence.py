class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        A  = sorted(arr)
        
        for i in range(1,len(A)-1):
            if A[i+1]-A[i] != A[i]-A[i-1]:
                return False
        return True