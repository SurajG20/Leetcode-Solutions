class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        N = len(matrix)
        
        # transpose, reversing along the diagonal
        for i in range(N):
            for j in range(i+1,N):
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
                
                
        print(matrix)
        
        # then reverse the whole matrix
        
        
        for arr in matrix:
            arr[:] = (arr[::-1])
            
        
    