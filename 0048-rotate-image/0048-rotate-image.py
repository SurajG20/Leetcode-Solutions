class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def rev_arr(l):
            i = 0
            j = len(l)-1
            while i < j:
                l[i] ,l[j] = l[j],l[i]
                i += 1
                j -= 1
            return l
        
        for i in range(len(matrix)):
            for j in range(i,len(matrix)):
                matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
                
        for ele in matrix:
            ele = rev_arr(ele)
            
        return matrix
    
       
        