class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        N = len(mat[0])
        M = len(mat)
        if N*M != r*c:
            return mat
        
        tmp = []
        
        
        k = 0
        output = [[[0] for _ in range(c)] for _ in range(r)]

        for i in range(M):
            for j in range(N):
                output[k//c][k%c] = mat[i][j]
                k +=1
        
        return output