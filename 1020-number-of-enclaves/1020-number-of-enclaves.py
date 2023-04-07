class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        Rows = len(grid)
        Cols = len(grid[0])
        
        def dfs(r,c):
            if r < 0 or c < 0 or r == Rows or c == Cols or (r,c) in visited or not grid[r][c]:
                return 0 
            
            visited.add((r,c))
            
            res = 1
            
            direct = [[1,0],[-1,0],[0,1],[0,-1]]
            
            for dr,dc in direct:
                res += dfs(r + dr,c + dc)
            return res
            
        visited = set()
        land = 0
        borderland = 0
        
        for i in range(Rows):
            for j in range(Cols):
                land +=  grid[i][j]
                
                if grid[i][j] and (i,j) not in visited and (i in [0,Rows-1] or j in [0,Cols-1]):
                    borderland += dfs(i,j)
                    
                    
        return land - borderland
                
