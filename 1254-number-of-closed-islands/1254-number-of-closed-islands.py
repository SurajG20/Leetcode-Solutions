class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        
        visited = set()
        res = 0
        def dfs(R,C):
            
            if R < 0 or C < 0 or R == ROWS or C == COLS:
                return 0
            if grid[R][C] or (R,C) in visited:
                return 1
            
            visited.add((R,C))
            return min(dfs(R+1,C),
                      dfs(R-1,C),dfs(R,C+1),dfs(R,C-1))
            
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and not grid[r][c]:
                    res += dfs(r,c)
                    
                    
        return res