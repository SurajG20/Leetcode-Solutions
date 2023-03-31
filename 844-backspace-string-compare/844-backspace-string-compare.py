class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def make(K):
            res = []
            
            for c in K:
                if c == "#":
                    if res:
                        res.pop()
                        
                else:
                    res.append(c)
                    
            return "".join(res)
        
        
        return make(s) == make(t)
