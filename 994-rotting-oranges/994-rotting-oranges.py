class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        Rows = len(grid)
        Cols = len(grid[0])
        
        time = 0
        fresh = 0
        
        q = deque()
        for i in range(Rows):
            for j in range(Cols):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append([i,j])
         
        
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        
        while q and fresh > 0:
            
            for i in range(len(q)):
                r,c = q.popleft()
                
                for dr,dc in directions:
                    
                    rows = r + dr
                    cols = c + dc
                    
                    if (rows<0 or rows >= Rows) or (cols < 0 or cols >= Cols) or grid[rows][cols] != 1:
                        continue
                    grid[rows][cols] = 2
                    q.append([rows,cols])
                    fresh -= 1
                    
            time += 1
            
        return time if fresh == 0 else -1
                
            
            