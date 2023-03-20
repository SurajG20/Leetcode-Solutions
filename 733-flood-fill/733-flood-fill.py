class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(R,C,S,image,color):
            if R < 0 or R >= rows or C < 0 or C >= cols:
                return
            elif image[R][C] != S:
                return 
                
            
            image[R][C] = color
            
            dfs(R-1,C,S,image,color)
            dfs(R+1,C,S,image,color)
            dfs(R,C-1,S,image,color)
            dfs(R,C+1,S,image,color)
            
        
        if image[sr][sc] == color:
            return image
        
        rows = len(image) 
        
        cols = len(image[0]) 
        
        src = image[sr][sc]
        
        dfs(sr,sc,src,image,color)
        return image
        