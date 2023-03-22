class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash = {}
        if len(set(s)) != len(set(t)):
            return False 
        for i in range(len(s)):
            if s[i] in hash and (hash[s[i]] != t[i]):
                return False    
            else:
                hash[s[i]] = t[i]
        return True
       
        
