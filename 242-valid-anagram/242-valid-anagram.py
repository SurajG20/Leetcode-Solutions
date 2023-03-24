class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash = {}
        
        for i in s:
            hash[i] = 1 + hash.get(i,0)
        for j in t:
            if j not in hash:
                return False
            hash[j] -= 1
        
        for key in hash:
            if hash[key] != 0:
                return False
                
        return True