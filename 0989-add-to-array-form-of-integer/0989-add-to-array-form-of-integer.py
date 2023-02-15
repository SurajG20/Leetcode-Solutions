class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
    
        # Linear Time and Linear Space solution
        temp = ""
        for i in num:
            temp += str(i)
        
        total = int(temp) + k
        
        res = []
        for i in str(total):
            res.append(int(i))
        return res
        