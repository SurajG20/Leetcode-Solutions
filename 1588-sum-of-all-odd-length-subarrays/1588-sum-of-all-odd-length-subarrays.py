class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        def sum(x,y):
            total = 0
            for ele in range(x,y+1):
                total += arr[ele]
                
            return total
        res = 0       
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                if (j - i )%2 ==0:
                    res += sum(i,j)
                    
        return res
                    
                    
                    