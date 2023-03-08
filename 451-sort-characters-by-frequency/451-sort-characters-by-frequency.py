class Solution:
    def frequencySort(self, s: str) -> str:
        mapp = {}
        
        for ch in s:
            mapp[ch] = 1  + mapp.get(ch,0)
            
        temp = []
        
        for key, val in mapp.items():
            temp.append((val,key))
        print(temp)
        
        helo = sorted(temp,reverse = True )
        
        res = ""
        for i, j in helo:
            for _ in range(i):
                res += j
                
            
        return res
            