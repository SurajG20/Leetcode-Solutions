class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # bfs function
        def bfs(n,m,visited,grid):
            visited[n][m] = 1 # mark the current nodes as visited
            queue = deque() # an array to keep track of upcoming nodes
            
            queue.append((n,m)) # append current node to it
            
            # while there are node in queue
            while queue:
                row,col = queue.popleft() # pop the elements
                
                # traversing in all eight directions
                directions = [(0,1), (0,-1), (-1,0), (1,0)]
                for d in directions:
                    newrow = row + d[0]
                    newcol = col + d[1]
                        
                        
                    # check if its a valid node 
                    if newrow >= 0 and newrow < N and newcol >= 0 and newcol < M and visited[newrow][newcol] != 1 and grid[newrow][newcol] == '1':
                        # mark this visited
                        visited[newrow][newcol] = 1
                        queue.append((newrow,newcol)) # also append it to queue 

                
            
                    
        N = len(grid) # number of row
        M = len(grid[0]) # number of column
        
        visited = [[0 for _ in range(M)] for _ in range(N)] # a array to keep track of visited node
        
        count = 0 # now of complete bfs we doing 
        
        for i in range(N):
            for j in range(M):
                if visited[i][j] != 1 and grid[i][j] == '1': # for each not visited and valid node 
                    count += 1 # increase the count 
                    bfs(i,j,visited,grid) # call the bfs for it  
                    
        return count
        