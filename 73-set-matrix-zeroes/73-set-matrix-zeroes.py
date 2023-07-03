class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
#         O(M+N) solution
        if not matrix:
            return []
        
        R = len(matrix)
        C = len(matrix[0])
        
        row_count = [False]*R
        col_count = [False]*C
        
        for i in range(R):
            for j in range(C):
                if matrix[i][j]==0:
                    row_count[i] = True
                    col_count[j] = True

                
                
        for row in range(R):
            for col in range(C):
                if row_count[row] or col_count[col]:
                    matrix[row][col] = 0
                    
        return matrix
        