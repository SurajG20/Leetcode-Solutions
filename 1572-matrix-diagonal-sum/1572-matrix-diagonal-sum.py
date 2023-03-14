class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        M = len(mat) # row
        N = len(mat[0]) # column
        
        res = 0
        mid = M//2
        for i in range(M):
            res += mat[i][i] # primary diagonal
            res += mat[M-1-i][i] # secondary diagonal
            
        if M % 2 == 1:
            res -= mat[mid][mid]

        return res