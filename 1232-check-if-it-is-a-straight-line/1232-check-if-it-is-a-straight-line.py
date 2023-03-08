class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        (x0, y0), (x1, y1) = coordinates[: 2]
        for x, y in coordinates:
            if (x1 - x0) * (y - y1) != (x - x1) * (y1 - y0):
                return False
        return True
        
#         if len(coordinates) == 2:
#             return True 
        
#         x1, y1 = coordinates[0][0], coordinates[0][1]
        
        
        
#         for K in range(1,len(coordinates)-1):
#             if (y1 - coordinates[K][1])//(x1-coordinates[K][0]) != (y1 - coordinates[K+1][1])//(x1-coordinates[K+1][0]):
#                 return False
#         return True 
            
            