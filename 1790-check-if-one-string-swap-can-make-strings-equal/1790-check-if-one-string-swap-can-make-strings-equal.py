class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        mapp1 = {}
        mapp2 = {}
        
        if s1 == s2:
            return True 
        for ch in s1:
            mapp1[ch] = 1 + mapp1.get(ch,0)
            
        for ch in s2:
            mapp2[ch] = 1 + mapp2.get(ch,0)
            
        if mapp1 != mapp2:
            return False
        
        count = 0
        
        i = 0
        j = 0
        
        while i < len(s1) and j < len(s2):
            if s1[i] == s2[j]:
                count +=1
            i += 1
            j += 1
            
        if count == len(s1)-2:
            return True 
        else:
            return False
        
        