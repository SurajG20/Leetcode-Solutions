class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        def dist(x1,y1,x2,y2):
            return abs(x1-x2)+abs(y1-y2)
        
        res = float('inf')
        curr = -1
        for i in range(len(points)-1,-1,-1):
            if points[i][0] == x or points[i][1] == y:
                current_dist = dist(points[i][0],points[i][1],x,y)
                
                if current_dist <= res:
                    res = current_dist
                    curr = i
                    
        return curr
                
                
                
                
                
                
                