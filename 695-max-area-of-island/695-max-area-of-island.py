class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(R,C):
            if 0 <= R < M and 0 <= C < N and grid[R][C] == 1:
                grid[R][C] = 0
                return 1 + dfs(R+1,C)+ dfs(R-1,C)+ dfs(R,C+1)+ dfs(R,C-1)
                
            else:
                return 0
        
        
        M = len(grid)
        N = len(grid[0])
        
        res = 0
        for i in range(M):
            for j in range(N):
                res = max(res,dfs(i,j))
                
        return res